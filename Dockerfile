FROM python:3.8.5

WORKDIR /app

COPY requirements.txt ./requirements.txt

COPY predict_page.py /app/

COPY explore_page.py /app/

COPY saved_steps.pkl /app/

COPY survey_results_public.csv /app/

RUN pip install -r requirements.txt

EXPOSE 8501

COPY app.py /app/

ENTRYPOINT ["streamlit", "run"]

CMD ["app.py"]


