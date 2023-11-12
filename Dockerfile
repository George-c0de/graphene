# Use the official Python 3.11 image as the base image
FROM python:3.11


# Create the application directory
RUN mkdir /app
RUN mkdir /app/staticfiles
RUN mkdir /app/media

# Install system dependencies
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Change the working directory to /app
WORKDIR /app

# Copy the application code to the container
COPY . /app

# Install Pipenv
RUN pip install pipenv

# Install project dependencies using Pipenv
COPY Pipfile Pipfile.lock /app/
RUN pipenv install --deploy --ignore-pipfile

RUN pipenv run pip install gunicorn

# Create the devops user

RUN chmod +x ./entrypoint.sh

# Specify the entrypoint and default command
ENTRYPOINT ["./entrypoint.sh"]

# Set the entry command to run Gunicorn
CMD ["pipenv", "run", "gunicorn", "--bind", "0.0.0.0:8000", "djangoProject.wsgi:application"]
