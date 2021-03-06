from django.db import models
from django import forms


class CurrencyChoice(models.Model):
    Currencies = [
        ('AUD', 'Австралійський долар'),
        ('CAD', 'Канадський долар'),
        ('CNY', 'Юань Женьмiньбi'),
        ('HRK', 'Куна'),
        ('CZK', 'Чеська крона'),
        ('DKK', 'Данська крона'),
        ('HKD', 'Гонконгівський долар'),
        ('HUF', 'Форинт'),
        ('INR', 'Індійська рупія'),
        ('IDR', 'Рупія'),
        ('IRR', 'Іранський ріал'),
        ('ILS', 'Новий ізраїльський шекель'),
        ('JPY', 'Єна'),
        ('KZT', 'Теньге'),
        ('KRW', 'Вона'),
        ('MXN', 'Мексіканський песо'),
        ('MDL', 'Молдовський лей'),
        ('NZD', 'Новозеландський долар'),
        ('NOK', 'Норвезька крона'),
        ('RUB', 'Російський рубль'),
        ('SAR', 'Саудівський рiял'),
        ('SGD', 'Сінгапурський долар'),
        ('ZAR', 'Ренд'),
        ('SEK', 'Шведська крона'),
        ('CHF', 'Швейцарський франк'),
        ('EGP', 'Єгипетський фунт'),
        ('GBP', 'Фунт стерлінгів'),
        ('USD', 'Долар США'),
        ('BYN', 'Бiлоруський рубль'),
        ('AZN', 'Азербайджанський манат'),
        ('RON', 'Румунський лей'),
        ('TRY', 'Турецька ліра'),
        ('XDR', 'СПЗ(спеціальні права запозичення)'),
        ('BGN', 'Болгарський лев'),
        ('EUR', 'Євро'),
        ('PLN', 'Злотий'),
        ('DZD', 'Алжирський динар'),
        ('BDT', 'Така'),
        ('AMD', 'Вiрменський драм'),
        ('IQD', 'Іракський динар'),
        ('KGS', 'Сом'),
        ('LBP', 'Ліванський фунт'),
        ('LYD', 'Лівійський динар'),
        ('MYR', 'Малайзійський ринггіт'),
        ('MAD', 'Марокканський дирхам'),
        ('PKR', 'Пакистанська рупія'),
        ('VND', 'Донг'),
        ('THB', 'Бат'),
        ('AED', 'Дирхам ОАЕ'),
        ('TND', 'Туніський динар'),
        ('UZS', 'Узбецький сум'),
        ('TWD', 'Новий тайванський долар'),
        ('TMT', 'Туркменський новий манат'),
        ('GHS', 'Ганських седі'),
        ('RSD', 'Сербський динар'),
        ('TJS', 'Сомонi'),
        ('GEL', 'Ларi'),
        ('XAU', 'Золото'),
        ('XAG', 'Срiбло'),
        ('XPT', 'Платина'),
        ('XPD', 'Паладiй')
    ]
    currency_code = models.CharField(max_length=3, choices=Currencies)
    currency_rate = models.FloatField(choices=Currencies)

    def __str__(self):
        return '{} to uah {}'.format(self.currency_code, self.currency_rate)

#TODO: add model for sync log Log(status="OK", sync_date=datetime.now(), sync_data=raw_data) 
