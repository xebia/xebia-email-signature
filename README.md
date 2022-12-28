# E-mail signature generator

## Pre-requirements

Docker or Docker toolbox (https://docs.docker.com/toolbox/)

## Build

```
docker build -t signature:latest .
```

## Run

```
docker run -it --rm --name xebia_signature signature:latest
```

Fill in the fields:

```
To generate a signature, enter the following details...
full name (John Doe): John Doe
e-mail (john.doe@xebia.com): john.doe@xebia.com
mobile phone (+31 6 12 34 56 78): +31 6 12 34 56 78
job role (Cloud Consultant): Cloud Consultant
link to your LinkedIn profile (https://www.linkedin.com/in/johndoe/): https://www.linkedin.com/in/johndoe/
```

And copy paste the generated output to your email client.
