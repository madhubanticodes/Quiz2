from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Attendance, Performance
from departments.models import Department

class Command(BaseCommand):
    help = "Generate 5 fake employees with attendance & performance"

    def handle(self, *args, **opts):
        fake = Faker()
        depts = [Department.objects.create(name=d, location=fake.city())
                 for d in ["HR","Engineering","Sales"]]
        for _ in range(5):
            emp = Employee.objects.create(
                first_name=fake.first_name(), last_name=fake.last_name(),
                email=fake.unique.email(), phone=fake.phone_number(),
                department=fake.random_element(depts),
                date_joined=fake.date_between('-2y','today'),
                salary=fake.random_int(50000,150000)
            )
            Attendance.objects.create(
                employee=emp, date=fake.date_this_month(),
                status=fake.random_element(['P','A']),
                check_in=fake.time(), check_out=fake.time()
            )
            Performance.objects.create(
                employee=emp, review_date=fake.date_this_year(),
                score=fake.random_int(1,10), remarks=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS("5 employees created"))
