import datetime
import inspect
import asyncio
import time

from qiwi_handler import loader

from qiwi_handler.handler import handler_check_pay
from qiwi_handler.utils.datetimes_utils import *
from qiwi_handler.exceptions import RequestError

already_proc = []


async def already_proc_insert(id_):
    already_proc.append(id_)
    await asyncio.sleep(60 * 60 * 13)
    try:
        already_proc.pop(id_)
    except Exception:
        pass

class CheckPayHandler:
    async def _check_pay_handler(self):

        '''message: str = None, wallets: list, amount: float = None,
        may_be_bigger = True, check_status = True'''

        self.headers = {
            'authorization': f'Bearer {self.token}',
        }
        await self.__proccess_check_pay(active=False)

        while True:
            await self.__proccess_check_pay()

    async def __proccess_check_pay(self, active=True):
        init_time = time.time() + 5
        for func, args in handler_check_pay:
            message, wallets, amount, may_be_bigger, check_status, operation, \
            updates_per_minute, rows_per_update = args
            params = {
                'rows': rows_per_update,
                "operation": operation
            }

            for wallet in wallets:
                await asyncio.sleep(60 / updates_per_minute)

                url = f'payment-history/v2/persons/{wallet}/payments'
                req = loader.Request(self.token)
                json = await req.do_get(url=url, headers=self.headers, params=params)
                histories = loader.convert_history(json)

                if "errorCode" in json:
                    raise RequestError(f'{json["errorCode"]}: {json["description"]}')

                for history in histories:
                    if history.data is None:
                        continue

                    sum = history.data.total
                    comment = history.data.comment
                    status = history.data.status
                    date = history.data.date
                    txn_id = history.data.txnId
                    person_id = history.data.personId

                    if txn_id in already_proc:
                        continue

                    if message:
                        if message is not comment:
                            continue

                    if amount:
                        if may_be_bigger:
                            if amount > sum.amount:
                                continue
                        elif amount != sum.amount:
                            continue

                    if check_status:
                        if status == "ERROR":
                            continue
                    # print(now(), from_datetime_to_time(date))
                    if now() >= from_datetime_to_time(date) >= (
                            now() - 60 * 60 * 12):
                        loop = asyncio.get_event_loop()
                        if time.time() > init_time:
                            return loop.create_task(already_proc_insert(history.data.txnId))
                        if txn_id in already_proc:
                            return
                        if active:
                            if inspect.iscoroutinefunction(func):
                                await func(pay=history)

                            else:
                                func(pay=history)


                        loop.create_task(already_proc_insert(history.data.txnId))
