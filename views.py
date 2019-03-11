from flask import Flask
from flask_restful import Resource, Api
from functions import fibonacci
from db import db, db_config
from models import FibData

# For benchmarking.
import time
import resource

app = Flask(__name__)
api = Api(app)
db_config(app)
db.init_app(app)

class Fib(Resource):
    ''' Handling the fibonacci numbers request '''
    def get(self, start_idx, end_idx):
        # Start the fibonacci.
        time_start = time.process_time()
        data = [fibonacci(n) for n in range(start_idx, end_idx)]
        time_elapsed = (time.process_time() - time_start)

        # To include the last fibonacci number.
        data.append(fibonacci(end_idx))

        # Include benchmark results.
        # data.append({'benchmark': {
        #     'time_elapsed': f'{time_elapsed: .5f}',
        #     }
        # })

        # Log to database
        fib_data = FibData(start=start_idx, end=end_idx)
        db.session.add(fib_data)
        db.session.commit()

        return data

class HealthCheck(Resource):
    ''' Handling the health information request '''
    def get(self):
        desease = 'Python'
        health_check = [
            {
                'first_name': 'Abdelaziz',
                'last_name': 'Abdelioua',
                'condition': 'Critical',
                'disease': 'Pythonlia',
                'symptoms': f'Addicted to a programming language that is called { desease }'
            }
        ]

        return health_check

api.add_resource(Fib, '/fib/<int:start_idx>/<int:end_idx>')
api.add_resource(HealthCheck, '/health')

if __name__ == "__main__":
    app.run(debug=True)