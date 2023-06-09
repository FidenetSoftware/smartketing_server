from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import models
from ...utils import convert_to_json
import json



#Obtener los resultados en base a la fecha:

#En base a la semana
async def get_twitch_extractions_by_day(db:Session, id:int, num_days: int):

    # Obtener la fecha y hora actual
    current_date = datetime.now()

    # Calcular la fecha de inicio (hace 24 horas)
    start_date = current_date - timedelta(days=num_days)

    # Definir la fecha de fin como la fecha y hora actual
    end_date = current_date

    query = db.query(models.Twitch_Extraction.created_at).filter(
        models.Twitch_Extraction.created_at.between(start_date, end_date),
        models.Twitch_Extraction.search_id == id).order_by(models.Twitch_Extraction.created_at)
    
    results = query.all()
    count = query.count()

    # Serialize the results using the custom conversion function
    results_json = json.dumps(results, default=lambda obj: convert_to_json(obj, ['created_at']))

    # Cargar la cadena JSON en un objeto Python
    parsed_data = json.loads(results_json)

    for data in parsed_data:
        data['count'] = count


#En base al mes y al año
async def get_twitch_extractions_by_date_range(db: Session, id: int, start_date: datetime, end_date: datetime):

    start = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end = datetime.strptime(end_date, '%Y-%m-%d %H:%M:%S')
    
    query = db.query(models.Twitch_Extraction.created_at).filter(
        models.Twitch_Extraction.created_at.between(start, end),
        models.Twitch_Extraction.search_id == id).order_by(models.Twitch_Extraction.created_at)

    results = query.all()
    count = query.count()

    
    # Serialize the results using the custom conversion function
    results_json = json.dumps(results, default=lambda obj: convert_to_json(obj, ['created_at']))

    # Cargar la cadena JSON en un objeto Python
    parsed_data = json.loads(results_json)

    for data in parsed_data:
        data['count'] = count

    return parsed_data