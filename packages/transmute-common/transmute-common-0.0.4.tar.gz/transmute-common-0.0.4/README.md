# A package to support ETL creation within [Transmute](https://github.com/finnor/Transmute)

## Prototypes
Prototypes are creator methods in Transmute for instantiating a model with its requisite fields while prefilling the model with the supplied fields. 

#### Usage
    from transmute_common.prototypes import patient as patientFactory

    patientInfo = {
        "patientId": "patient-01",
        "sex": "Male"
    }

    patient = patientFactory.create(patientInfo)

    print(patient)

#### Output

    {
        "patientId": "patient-01",
        "sex": "Male",
        "race": None,
        "ethnicity": None,
        ...
    }

#### Prototype Models

* patient
* sample
* smallVariantAnalysis
* smallVariant
* cnvAnalysis
* cnv
* fusionAnalysis
* fusion
