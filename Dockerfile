FROM public.ecr.aws/lambda/python:3.9
ENV ENV_URL=tw.yahoo.com
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

COPY index.py ${LAMBDA_TASK_ROOT}

CMD [ "index.lambda_handler" ]