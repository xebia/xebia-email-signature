from unittest import TestCase

from xebia_email_signature.inline_images import inline_images
from bs4 import BeautifulSoup


class TestInlineImages(TestCase):
    def test_inline_images(self):
        html_doc = """<html>
        <head>
        <title>My webpage</title>
        </head>
        <body>
        <img src="https://assets.oblcc.com/xebia/facebook.png">
        <img src="https://assets.oblcc.com/xebia/instagram.png">
        </body>
        </html>"""

        base_url = "https://xebia.com/"

        expected_output = """<html>
        <head>
        <title>My webpage</title>
        </head>
        <body>
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAYAAAByUDbMAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TRakVBzuIOGSogmBBVMRRq1CECqFWaNXB5KV/0KQhSXFxFFwLDv4sVh1cnHV1cBUEwR8QVxcnRRcp8b6k0CLGC4/3cd49h/fuA4R6mWlWxzig6baZSsTFTHZV7HpFAD2IYBQhmVnGnCQl4Vtf99RNdRfjWf59f1avmrMYEBCJZ5lh2sQbxNObtsF5nzjCirJKfE48ZtIFiR+5rnj8xrngssAzI2Y6NU8cIRYLbay0MSuaGvEUcVTVdMoXMh6rnLc4a+Uqa96TvzCc01eWuU5rCAksYgkSRCioooQybMRo10mxkKLzuI9/0PVL5FLIVQIjxwIq0CC7fvA/+D1bKz854SWF40Dni+N8DANdu0Cj5jjfx47TOAGCz8CV3vJX6sDMJ+m1lhY9Avq2gYvrlqbsAZc7wMCTIZuyKwVpCfk88H5G35QF+m+B0Jo3t+Y5Th+ANM0qeQMcHAIjBcpe93l3d/vc/u1pzu8HQSdyk+bIThoAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfnAQsUKS6uS7ajAAAB20lEQVQ4y+WTsWtTURjFz7nvtU1CUpcWoSR1URwUddHRQcTFxcEMoibRQWxMKlordhQRFCNKiKkdLClBQfofOOvkElBwcAm8VigFp1Tb+u49DpqYQUiibn7bdzj3d8+BewkA06nz+y3MjJE8kRH0OZQ2RQpiqbJSe8epZOaAZzjrvn6Zqq4vtzDg5MfTcROJPbHSQ98Hboxsucul9eWNXgevJdPR0ERPStxLMQEA8vgqshnmt4Y4b0SqtFbvCbo0cWbsG2MvJBM62Zeh2b4v4DmcO15aq2+IlN9vnWFv+LpzvF1drTXa2tWJTMJ67Hj6hgnaWV1dagBAMZk5AqAQkhbSm4FhBDsRnMFp6zD3NFha7fb0hE0nc3ucwSFAo7+eBH2fOFGYzLWMQ6O8UvsIAKZnPaNzlHxa704ngccyqUDO7RBdeqCa1prX1U+LQXt/3Kw1ATQLuy4cg1PY1nsnE7aNZ+8VU9mZtlZI5U4VktkFOHfLUUHfySrB0t0fgOxi1xVHh+DPPQqefe72GvzD+Q9glGgA+fnxdPxvQPnxdFyGNHKomEh0obj77OifgG6OXUyYaGzeOj0gAFyZzO6jOAvKgzDy+4+OwwTe/lwPEvzgqBbF0MCWykH9/XdiaL6rB9s8+wAAAABJRU5ErkJggg=="/>
        <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABMAAAATCAYAAAByUDbMAAABhWlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw1AUhU9TRakVBzuIOGSogmBBVMRRq1CECqFWaNXB5KV/0KQhSXFxFFwLDv4sVh1cnHV1cBUEwR8QVxcnRRcp8b6k0CLGC4/3cd49h/fuA4R6mWlWxzig6baZSsTFTHZV7HpFAD2IYBQhmVnGnCQl4Vtf99RNdRfjWf59f1avmrMYEBCJZ5lh2sQbxNObtsF5nzjCirJKfE48ZtIFiR+5rnj8xrngssAzI2Y6NU8cIRYLbay0MSuaGvEUcVTVdMoXMh6rnLc4a+Uqa96TvzCc01eWuU5rCAksYgkSRCioooQybMRo10mxkKLzuI9/0PVL5FLIVQIjxwIq0CC7fvA/+D1bKz854SWF40Dni+N8DANdu0Cj5jjfx47TOAGCz8CV3vJX6sDMJ+m1lhY9Avq2gYvrlqbsAZc7wMCTIZuyKwVpCfk88H5G35QF+m+B0Jo3t+Y5Th+ANM0qeQMcHAIjBcpe93l3d/vc/u1pzu8HQSdyk+bIThoAAAAGYktHRAD/AP8A/6C9p5MAAAAJcEhZcwAADdcAAA3XAUIom3gAAAAHdElNRQfnAQsULBASXV9NAAADGklEQVQ4y52UT2hcVRTGv+/eN+/NTNRg/2gJM9NoXaVoF12ldOXGlSDKLM1MRCftZKalYKALoZtWpRorzGSiA00zU+OmCxcKRRCEKqi4EBIUF6FNMk8tSUz/ZOjM67x7j4tYM1Vqot/2u/fH+c499xAARlOZ/RSOUawSMoptiiJtobIQjJf96TkWEtmnQXuSnjlamp+5jf+o/O70QyraU4ZgnMXEUN0ErTzdmEfFdwDGAVHbqgwQS1Rjgf225aqyI6RUVi41RxOZM1bMmxX/o/l/A4ymMvsJDtDC3OyYz3s9VbudiF1xl4PNChTk0a1AaaQ1BacJe0OU7Op1mYHIT5E107fB+FNCylax9jy1xwFlpbRU/0JZfgmonaCyETEEAGerthQSmReFGFTAb83m9XqPE+8rJrJvG9rdEHxGqgP3DnfDYsdSmYPGyMLEL/XfAaCQzFQo+NrRPB2ENhV34hUFnuiou6vBnWYY9XbsU8BzoRgCajMmBb1W+Ao0XgWAwt7hZynyY8mvzby/MH1z0q/PunBGrLJjk0sf34jSE0WZgsgTMa2dv/UM163gU1rVAAAaM2Ah33dnPuefX4PQA4DKyqUmiDkhv+lYdO6DAQApdwQ2DgCWnFVUh7v9I4+//BgowWYYCbv9+2A9Lf0DyUMAMNGoXRGgv5DMHsn3DSfzqaHDEVdXRUfOAMCxvcODoJp7IOzs6tS6CNaPJoaeAYByo1aE2EVqm6PwgNbITlw7v3gKp5RYe7zjuBe67/9jNHra+o1WzF4s9GdPlhemfy779csALt/zcwdzkbXlhXNGeKF6tXqrkMo+GHZ2dWo992Qu44XBu6PJ7DJhPmHHWTReuEtbPSjLwfMA36v4019tvJxVHUaECLtGA1grJjP7AKB6tXqrtFR7jRoXSXXIumaMol4AxN/Z6H+p1NgApZHWIAc6O/SvApCF5NCMbbdGPO8Rt4PwLRAPb+Nn/LU1RKkPo+3wuyDCSUcsyozFPwjddr48PzPyf/ZZOxqv0OpxAkAxNTwgYl8HoAHEtgsS4i4FxoiMT/r12T8Af6lZuWbOAr8AAAAASUVORK5CYII="/>
        </body>
        </html>"""
        result = inline_images(html_doc, base_url)
        souped_doc = BeautifulSoup(expected_output, "html.parser")
        self.assertEqual(str(souped_doc), result)
