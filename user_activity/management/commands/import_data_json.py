from django.core.management.base import BaseCommand, CommandError
from user_activity.models import CLASSES

import json
import jsonschema
import os


class DbAction:

    def db_import(self, **kwargs):
        table_name = kwargs.pop('table')
        try:
            result = CLASSES.get(table_name).objects.filter(**kwargs)[0]
        except IndexError:
            result = None
        if not result:
            table = CLASSES.get(table_name)(**kwargs)
            table.save()
            return table
        return result


class Command(BaseCommand, DbAction):
    help = 'Imports data from JSON file.'

    def add_arguments(self, parser):
        parser.add_argument('json_file', nargs='+', type=str)

    def handle(self, *args, **options):
        for json_file in options['json_file']:
            try:
                schema_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.json')
                schema = json.load(open(schema_path, 'r'))
                activity_data = json.load(open(json_file, 'r'))

                try:
                    jsonschema.validate(activity_data, schema)
                except jsonschema.exceptions.ValidationError as e:
                    raise CommandError(f'JSON schema not correct - {str(e)}')

                for user_data in activity_data['members']:
                    data = {
                        "table": "User",
                        "id": user_data['id'],
                        "real_name": user_data['real_name'],
                        "tz": user_data['tz']
                    }
                    user = self.db_import(**data)

                    for period in user_data['activity_periods']:
                        period_data = {
                            "table": "ActivityPeriod",
                            "start_time": period['start_time'],
                            "end_time": period['end_time'],
                            "user": user
                        }
                        self.db_import(**period_data)

            except FileNotFoundError as e:
                raise CommandError(f'{json_file} not found! {str(e)}')
            except Exception as e:
                raise CommandError(f'ERROR {str(e)}')
