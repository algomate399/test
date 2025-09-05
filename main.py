from DeltaApi import run
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask, render_template,request
import threading
import asyncio
from pytz import timezone


def primary_task_1():
        run()


app = Flask(__name__)
connected = False
passkey = '141990'
scheduler = None

async def on_tick():
    while connected:
        await asyncio.sleep(1)


@app.route('/')
def Homepage():
    title = 'Algomate-GPT(AI Driven Model)'
    return render_template('index.html', title=title)


@app.route('/on_connect', methods=['POST'])
def On_connect():
    global connected, scheduler
    status = ''
    json_data = request.get_json()

    if json_data['passkey'] == passkey:
        if not connected:
            connected = True

            # Create and start the asyncio event loop
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

            # Initialize the AsyncIOScheduler with the loop
            scheduler = AsyncIOScheduler(event_loop=loop)

            # Add tasks to the scheduler
            scheduler.add_job(primary_task_1 , CronTrigger(hour=2 , minute=45 , timezone=timezone('Asia/Kolkata')))

            # Start the scheduler
            scheduler.start()

            # Start the asyncio loop in a background thread
            threading.Thread(target=loop.run_forever, daemon=True).start()

            # Schedule the on_tick coroutine
            asyncio.run_coroutine_threadsafe(on_tick(), loop)

            status = 'engine is running'
        else:
            status = 'engine stopped'
            connected = False
    else:
        status = 'Incorrect Pass key'

    return status


@app.route('/get_connection_status')
def get_connection_status():
    if connected:
        return 'engine is running'
    else:
        return 'not connected'


if __name__ == '__main__':
    app.run(debug=True)

