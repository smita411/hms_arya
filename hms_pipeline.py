
from pyspark import pipelines as dp

@dp.materialized_view(
    name="patient"
)
def patient():
    return (
        spark.read.table("hms_arya.bronze.patients")
             .filter("patient_id IS NOT NULL")
             .dropDuplicates(["patient_id"])
    )

@dp.materialized_view(
    name="admission"
)
def admission():
    return (
        spark.read.table("hms_arya.bronze.admissions")
             .filter("admission_id IS NOT NULL")
             .filter("patient_id IS NOT NULL")
             .filter("admit_date IS NOT NULL")
             .dropDuplicates(["admission_id"])
    )

@dp.materialized_view(
    name="billing"
)
def admission():
    return (
        spark.read.table("hms_arya.bronze.billing")
             .filter("billing_id IS NOT NULL")
             .filter("patient_id IS NOT NULL")
             .filter("amount_paid IS NOT NULL")
             .dropDuplicates(["billing_id"])
             
    )

@dp.materialized_view(
    name="doctors"
)

def doctors():
    return (
        spark.read.table("hms_arya.bronze.doctors")
             .filter("doctor_id IS NOT NULL")
             .dropDuplicates(["doctor_id"])
             
    )
@dp.materialized_view(
    name="nuurses"
)

def doctors():
    return (
        spark.read.table("hms_arya.bronze.nurses")
             .filter("nurse_id IS NOT NULL")
             .dropDuplicates(["nurse_id"])
             
    )
@dp.materialized_view(
    name="appointments"
)

def doctors():
    return (
        spark.read.table("hms_arya.bronze.appointments")
             .filter("appointment_id IS NOT NULL")
             .dropDuplicates(["appointment_id"])
             
    )
