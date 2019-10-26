import requests
import json
from django.core.management.base import BaseCommand, CommandError
from calculator.models import CurrencyChoice

#json_string = json.dumps(data)

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        #FIXME: this MUST be management command
        requestNBU = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
        print(requestNBU.encoding)
        raw_data = requestNBU.json()
 #       print(requestNBU.json())

        for data_line in raw_data:
            print(data_line)
            print(data_line['cc'])
            print(data_line['rate'])

            data_line, created = CurrencyChoice.objects.update_or_create(
                currency_code = data_line['cc'],
                defaults = {'currency_rate' : data_line['rate']},
            )


            #TODO: 1) create or update logic
            #TODO: 2) fix troubles with loop
            '''get_value = CurrencyChoice(
                currency_name = data_line['txt'],
                currency_code = data_line['cc'],
                currency_rate = data_line['rate'])
            #params
            get_value.upa()'''
            
            

            
            #TODO: 1) Add rate property to model
            #TODO: 2) Use data from dict to fill and save the model
           
        self.stdout.write(self.style.SUCCESS('Successfully imported'))
'''
#json_string = json.dumps(data)

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        #FIXME: this MUST be management command
        requestNBU = requests.get('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json')
        print(requestNBU.encoding)
        raw_data = requestNBU.json()
 #       print(requestNBU.json())
        for data_line in raw_data:
            print(type(data_line))
#TODO: save results to DB:)
        self.stdout.write(self.style.SUCCESS('Successfully imported'))

    def Pars(self, *args, **options):
        data = response.text
        parsed = json.loads(data)
        cc_id = parsed["requestNBU"][0]["cc"]
        cc_text = parsed["requestNBU"][0]["txt"]
        cc_rate = parsed["requestNBU"][0]["rate"]

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
    # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)
        for currency in parsed:
            for index in parsed[product]:
                for element in parsed[product][index]:'''
