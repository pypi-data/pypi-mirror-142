from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import func, distinct
from sqlalchemy import over
from sqlalchemy import inspect
from sqlalchemy.orm import scoped_session

from sqlalchemy import Column, Boolean, Date, DateTime, Float, Integer, Text, String

from sqlalchemy.orm import aliased
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import joinedload

import hashlib
import uuid
import json
import datetime
from sqlalchemy import select, update, delete, Index
import os
import pathlib

"""
Kraken_db api

methods:

- get:
    - input:

- search:



"""


"""

engine = create_engine('sqlite:///test.sqlite?''uri=true&check_same_thread=False&timeout=10', echo=False)

Base = declarative_base()


Session = sessionmaker(bind=engine)
session = Session()
"""

"""
Class declaration
"""
Base = declarative_base()


class DB_entities(Base):
    __tablename__ = 'DB_entities'
    __table_args__ = (
        Index("record_type_e", "record_type"),
        Index("record_id_e", "record_id"),
        Index("ref_id_e", "ref_id"),
        {'extend_existing': True},
    )


    id = Column(String)
    record_type = Column(String)
    record_id = Column(String)
    ref_id = Column(String, primary_key = True)
    #observations = relationship('DB_observation', backref='ref_id')


class DB_observation(Base):
    __tablename__ = 'DB_observations'
    __table_args__ = (
        Index("key", "key"),
        Index("value", "value"),
        Index("record_type", "record_type"),
        Index("record_id", "record_id"),
        Index("hash", "hash"),
        {'extend_existing': True},
    )


    id = Column(String)
    observation_id = Column(String)
    ref_id = Column(String, ForeignKey('DB_entities.ref_id'))
    
    record_type = Column(String)
    record_id = Column(String)
    key = Column(String)
    value = Column(String)
    value_str = Column(String)
    value_float = Column(Float)
    value_date = Column(DateTime)
    value_json = Column(String)
    value_id = Column(String)
    value_type = Column(String)
    
    datasource = Column(String)
    agent = Column(String)
    instrument = Column(String)
    object = Column(String)
    result = Column(String)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    valid = Column(Boolean)

    credibility = Column(Float)
    created_date = Column(DateTime)    
    hash = Column(String, primary_key = True)
    observation_date = Column(DateTime)

    entity = relationship("DB_entities", back_populates = "observations")

    def _asdict(self):
        record = {c.key: getattr(self, c.key, None) for c in inspect(self).mapper.column_attrs}

        record.pop('id')
        record.pop('ref_id')

        if record.get('value_str', None) is not None:
            record['value'] = record.get('value_str', None)
            
        elif record.get('value_float', None) is not None:
            record['value'] = record.get('value_float', None)

        elif record.get('value_date', None) is not None:
            record['value'] = record.get('value_date', None)

        elif record.get('value_json', None) is not None:
            record['value'] = json.loads(record.get('value_json', None))

        elif record.get('value_type', None) is not None:
            record['value'] = {
                '@type': record.get('value_type', None),
                '@id': record.get('value_id', None)
            }
                               
        return record



DB_entities.observations = relationship("DB_observation", order_by = DB_observation.ref_id, back_populates = "entity")







class Kraken_db:
    
    def __init__(self, filepath):


        self.filepath = filepath

        
        self.initialize_db_engine()
       

    def initialize_db_engine(self):

        # Create file for db and create session
        
        os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
        
        self.engine = create_engine('sqlite:///' + self.filepath + '.sqlite?uri=true&check_same_thread=False&timeout=10', echo=False)
        session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(session_factory)
        self.session = self.Session()
        Base.metadata.create_all(self.engine)

    def destroy_db(self):
        file_to_rem = pathlib.Path(self.filepath + '.sqlite')
        file_to_rem.unlink(missing_ok = True)
        return
    
    """
    API - DB_observations
    """



    def rollback(self):
        self.Session.rollback()
        a=1






    def get(self, record_type = None, record_id = None, key = None, value = None):
        # Get DB_observations matching conditions

        self.Session()
        query = self._get_observations(record_type, record_id, key, value)
        records = self._to_dict(query)
        self.Session.remove()
        
        return records


    def get_max(self, record_type = None, record_id = None, key = None, value = None):
        """Return max DB_observation
        """

        self.Session()
        query = self._get_max_observations(record_type, record_id, key, value)
        records = self._to_dict(query)
        self.Session.remove()

        return records


    def get_summary(self, record_type = None, record_id = None, key = None, value = None):
        """Return object with max DB_observation for each key
        """
        self.Session()
        query = self._get_summary(record_type, record_id, key, value)
        records = self._to_dict(query)
        self.Session.remove()

        return records


    def get_summary_by_value(self, record_type = None, record_id = None):
        """Return object with max DB_observation for each key value combination
        """
        self.Session()
        query = self._get_summaries_by_value(record_type, record_id)
        records = self._to_dict(query)
        self.Session.remove()

        return records



    """
    API - entities
    """


    def search(self, params, order_by = None, order_direction = None, limit = None, offset = None):

        self.Session()
        query = self._search(params, order_by, order_direction, limit, offset)

        records = self._to_dict(query)
        self.Session.remove()

        return records


    def search_summary(self, params, order_by = None, order_direction = None, limit = None, offset = None):
        """Search and return summaries
        """
        
        self.Session()
        query = self._search(params, order_by, order_direction, limit, offset)

        query = self._get_summaries(query)

        records = self._to_dict(query)
        self.Session.remove()

        return records




    def search_first(self,params, order_by = None, order_direction = None, limit = None, skip = None):

        self.Session()
        query = self._search(params, order_by, order_direction, 1, 0)

        records = self._to_dict(query)
        self.Session.remove()

        return records



    def post(self, record):
        """Post an DB_observation. Need ot be committed
        """

        self.Session()
        result = self._post_observation_from_record(record)
        
        self.commit()
        self.Session.remove()

        return result


    def update(self, old_record_type, old_record_id, new_record_type, new_record_id):
        """Changes record_id and related references
        """

        self.Session()
        self._update(old_record_type, old_record_id, new_record_type, new_record_id)

        self.commit()
        self.Session.remove()

        return


    def commit(self):
        """Commmit posting of DB_observations
        """
        self._commit()

        return


    def update_id(self, old_id, new_id):
        """Replaces the ids of the observations
        """

        self.Session()
        self.Session.execute(update(DB_observation).where(DB_observation.record_id == old_id).values(record_id=new_id))

        self.Session.remove()


    def delete(self, observations):

        self.Session()
        if not isinstance(observations, list):
            observations = [observations]

        for i in observations:
            if i.get('observation_id', None):
                self.Session.execute(delete(DB_observation).where(DB_observation.observation_id == i.get('observation_id', None)))

        self.Session.remove()


    """
    Methods
    """

    def list_record_types(self):
        """Return list of dict with record_types and number for each
        """
        query = self.Session.query(func.count(distinct(DB_entities.record_id)), DB_entities.record_type).group_by(DB_entities.record_type).all()

        records = []
        for n, t in query:

            record = {
                'record_type': t,
                'n': n
            }
            records.append(record)

        return records


    def _get_observations(self, record_type, record_id, key, value):
        """ Return DN_entities matching condition
        """

        
        query = self.Session.query(DB_entities).join(DB_observation)


        if record_type:
            query = query.filter(DB_observation.record_type == record_type)

        if record_id:
            query = query.filter(DB_observation.record_id == record_id)
            
        if key:
            query = query.filter(DB_observation.key == key)

        if value:
            query = query.filter(DB_observation.value == value)


        return query



    def _get_max_observations(self, record_type, record_id, key, value):

        query = self._get_observations(record_type, record_id, key, value)

        query.order_by(DB_observation.credibility.desc()).order_by(DB_observation.credibility.created_date())

        # Limit
        query = query.limit(1)

        return query


    def _get_summary(self, record_type = None, record_id = None, key = None, value = None):

        query1 = self._get_observations(record_type, record_id, key, value)
        
        query = self._get_summaries(query1)


        return query

    def _get_summaries(self, query):
        """Returns best DB_observation for each keys of records in scope of query
        """
        
        subquery1 = query

        subquery1 = subquery1.subquery()

        # Filter for top credibility
        
        subquery2 = self.Session.query(subquery1)
        subquery2 = subquery2.group_by(subquery1.c.record_type)
        subquery2 = subquery2.group_by(subquery1.c.record_id)
        subquery2 = subquery2.group_by(subquery1.c.key)
        subquery2 = subquery2.having(func.max(subquery1.c.credibility) == subquery1.c.credibility)
        subquery2 = subquery2.subquery()
        
        # Filter for top created date
        subquery3 = self.Session.query(subquery2)
        subquery3 = subquery3.group_by(subquery2.c.record_type)
        subquery3 = subquery3.group_by(subquery2.c.record_id)
        subquery3 = subquery3.group_by(subquery2.c.key)
        subquery3 = subquery3.having(func.max(subquery2.c.created_date) == subquery2.c.created_date)

        return subquery3


    def _get_summaries_by_value(self, record_type, record_id):
        """Returns best DB_observation for each keys/values of records in scope of query
        """

        
        # Get max cred for each key
        obs1 = aliased(DB_observation)

        subquery1 = self.Session.query(obs1)
        subquery1 = subquery1.filter(obs1.record_type == record_type)
        subquery1 = subquery1.filter(obs1.record_id == record_id)
        subquery1 = subquery1.subquery()
        
        # Filter for top credibility
        subquery2 = self.Session.query(subquery1)
        subquery2 = subquery2.group_by(subquery1.c.key)
        subquery2 = subquery2.group_by(subquery1.c.value)
        subquery2 = subquery2.having(func.max(subquery1.c.credibility) == subquery1.c.credibility)
        subquery2 = subquery2.subquery()
        
        # Filter for top created date
        subquery3 = self.Session.query(subquery2)
        subquery3 = subquery3.group_by(subquery2.c.key)
        subquery3 = subquery3.group_by(subquery2.c.value)
        subquery3 = subquery3.having(func.max(subquery2.c.created_date) == subquery2.c.created_date)

        # Order
        subquery3 = subquery3.order_by(subquery2.c.key)
        subquery3 = subquery3.order_by(subquery2.c.credibility.desc())
        subquery3 = subquery3.order_by(subquery2.c.created_date.desc())

        return subquery3




    def _post_observation_from_record(self, record):

        
        if type(record) is list:
            for i in record:
                self._post_observation_from_record(i)
            return


        if not record.get('created_date', None):
            record['created_date'] = datetime.datetime.now()

        record_ref_id = str(record.get('record_type', None)) + '/' + str(record.get('record_id', None))

        # Generate hash

        hash_record = {}
        for i in record:
            if i not in ['created_date', 'observation_id', 'hash']:
                hash_record[i] = record[i]
        
        dhash = hashlib.md5()

        encoded = json.dumps(hash_record, default = str, sort_keys=True).encode()
        dhash.update(encoded)
        hash_value = dhash.hexdigest()
        
        

        entity = DB_entities(
            ref_id = record_ref_id,
            record_type = record.get('record_type', None),
            record_id = record.get('record_id', None),
        )


        # Generate class instance
        obs = DB_observation(
            observation_id = record.get('observation_id', None),
            ref_id = record_ref_id,
            datasource = record.get('datasource', None),
            agent = record.get('agent', None),
            instrument = record.get('instrument', None),
            object = record.get('object', None),
            result = record.get('result', None),
            start_time = record.get('start_time', None),
            end_time = record.get('end_time', None),
            valid = record.get('valid', None),

            record_type = record.get('record_type', None),
            record_id = record.get('record_id', None),
            key = record.get('key', None),
            credibility = record.get('credibility', None),
            created_date = record.get('created_date', None),
            hash = hash_value    
            )


        # Store value
        value = record.get('value', None)
        try:
            value = float(value)
        except:
            a1=1

        if not value:
            obs.value = None
        
        if isinstance(value, dict) and '@type' in value.keys() and '@id' in value.keys():
            obs.value_type = value.get('@type', None)
            obs.value_id = value.get('@id', None)

        elif isinstance(value, dict):
            obs.value_json = json.dumps(value, default = str)
        
        elif isinstance(value, str):
            obs.value_str = value
        
        elif isinstance(value, (int, float)):
            obs.value_float = value
        
        elif isinstance(value, datetime.datetime):
            obs.value_date = value
        
        
        self.Session.merge(entity)
        self.Session.merge(obs)
        self.Session.commit()
        return obs.observation_id



    
    def _update(self, old_record_type, old_record_id, new_record_type, new_record_id):

        
        # Step 1. Update record_ids
        query = self.Session.query(DB_observation)
        query = query.filter(DB_observation.record_type == old_record_type)
        query = query.filter(DB_observation.record_id == old_record_id)

        query = query.update(
            {
                DB_observation.record_type: new_record_type, 
                DB_observation.record_id: new_record_id
                })


        # Step 2. Update references to record_ids
        old_record = {
            '@type': old_record_type,
            '@id': old_record_id
        }
        old_record = json.dumps(old_record, default=str)

        new_record = {
            '@type': new_record_type,
            '@id': new_record_id
        }
        new_record = json.dumps(new_record, default=str)

        query = self.Session.query(DB_observation)
        query = query.filter(DB_observation.value == old_record)

        query = query.update(
            {
                DB_observation.value: new_record }
                )


    def _commit(self):
        
        self.Session.commit()



    def _search(self, params, order_by = None, order_direction = None, limit = None, offset = None):
        

        query = self.Session.query(DB_entities).join(DB_observation)

        ent = DB_observation

        for key, operator, value in params:

            query = self._sub_search(query, ent, key, operator, value)
            
        query = query.distinct()


        # apply order_by
        if order_by:
            if order_direction not in ['asc', 'desc']:
                order_direction = 'asc'

            query = query.order_by(getattr(getattr(DB_observation, order_by), order_direction)())
        
        query = query.distinct(DB_entities.ref_id)

        # apply limit and offset
        if limit:
            query = query.limit(limit)
        if offset:
            query = query.offset(offset)

        return query



    def _sub_search(self, sub_query, ent, key, operator, value):
        
        
        if key == 'record_type':
                sub_query = sub_query.filter(ent.record_type.like(value))
        elif key == 'record_id':
            sub_query = sub_query.filter(ent.record_id.like(value))
        
        elif key == 'created_date':
            sub_query = sub_query.filter(ent.created_date.like(value))   
        elif key == 'key':
            sub_query = sub_query.filter(ent.key.like(value))   
        elif key == 'value':
            sub_query = sub_query.filter(ent.value.like(value))   

        else:
            # text
            if isinstance(value, dict) and value.get('@type', None) and value.get('@id', None):
                record_type = value.get('@type', None)
                record_id = value.get('@id', None)

                if operator in ['eq', '==']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_type == record_type)  
                    sub_query = sub_query.filter(ent.value_id == record_id)  

                elif operator in ['ne', '!=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_type == record_type)  
                    sub_query = sub_query.filter(ent.value_id != record_id)
            
            
            elif isinstance(value, str):
                if operator in ['eq', '==']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_str.like(value))
                
                elif operator in ['ne', '!=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_str.notlike(value))

                elif operator in ['c', 'contains']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_str.contains(value))  
                elif operator in ['nc', 'not contains']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(~ent.value_str.contains(value))
                    
                elif operator in ['in']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_str in value)  


                    
            # if number
            elif isinstance(value, (int, float)):

                if operator in ['eq', '==']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float == value) 
                
                elif operator in ['ne', '!=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float != value) 

                
                elif operator in ['gt', '>']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float > value)            

                elif operator in ['ge', '>=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float >= value)   

                elif operator in ['lt', '<']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float < value)            

                elif operator in ['le', '<=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float <= value)   

                elif operator in ['contains']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(value in ent.value_float)  

                elif operator in ['in']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_float in value)  

            # if date
            elif isinstance(value, datetime.datetime):
                if operator in ['eq', '==']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date == value)  

                elif operator in ['ne', '!=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date != value)  

                elif operator in ['gt', '>']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date > value)            
                elif operator in ['ge', '>=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date >= value)   

                elif operator in ['lt', '<']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date < value)            
                elif operator in ['le', '<=']:
                    sub_query = sub_query.filter(ent.key == key)
                    sub_query = sub_query.filter(ent.value_date <= value)  

            

        
        return sub_query



    """
    Methods: transformation
    """


    def _to_dict_single(self, record):


        if type(record) is dict:

            result = {}
            for c in record.keys():
                result[c] = getattr(record, c, None)


            result.pop('id')
            result.pop('ref_id')

            return result

        else:
            result = record._asdict()

        #         

        return result



    def _to_dict(self, querys):
        # COnvert sqlalchemy classes to dicts
        records = []
        for r in querys:
            for o in r.observations:
                record = self._to_dict_single(o)
                records.append(record)

        return records


