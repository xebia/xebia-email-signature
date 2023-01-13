include Makefile.image
REGION = eu-west-1
AWS_ACCOUNT_ID = $(shell aws sts get-caller-identity --query Account --output text)
REGISTRY_HOST = $(AWS_ACCOUNT_ID).dkr.ecr.$(REGION).amazonaws.com

deploy-pipeline:  ## deploys the CI/CD pipeline
	aws cloudformation deploy \
		--stack-name $(NAME)-pipeline \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset \
		--template-file cloudformation/cicd-pipeline.yaml

delete-pipeline:  ## deletes the CI/CD pipeline
	aws cloudformation delete-stack \
		--stack-name $(NAME)-pipeline
	aws cloudformation wait stack-delete-complete \
		--stack-name $(NAME)-pipeline

deploy-app: cloudformation/xebia-email-signature.yaml ## deploys the application
	aws cloudformation deploy \
		--role-arn arn:aws:iam::$(AWS_ACCOUNT_ID):role/CloudformationRole \
		--stack-name $(NAME) \
		--capabilities CAPABILITY_IAM \
		--no-fail-on-empty-changeset \
		--template-file cloudformation/$(NAME).yaml

cloudformation/xebia-email-signature.yaml: src/app_runner_custom_domain_resource_provider/__init__.py
	pipenv run aws-cfn-update lambda-inline-code  \
		--resource AppRunnerCustomDomainProvider  \
		--file $? $@

deploy-certificate:  ## deploys the certificate
	aws cloudformation deploy \
                --region us-east-1 \
                --role-arn arn:aws:iam::$(AWS_ACCOUNT_ID):role/CloudformationRole \
                --stack-name $(NAME)-certificate \
                --no-fail-on-empty-changeset \
                --template-file cloudformation/certificate.yaml

delete-app:  ## deletes the application
	aws cloudformation delete-stack \
		--stack-name $(NAME)
	aws cloudformation wait stack-delete-complete \
		--stack-name $(NAME)

update-image-reference: ## updates the image reference in the deployment
	cru  --verbose update --image-reference $(IMAGE):$(VERSION) cloudformation
