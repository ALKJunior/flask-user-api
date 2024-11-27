from sqlalchemy import Column, String, Integer, Boolean, DateTime, func, Enum as SQLEnum
from app.commons.config import Base, session_factory
from app.commons.hash import hash
from app.commons.jwt import create_jwt_token, validate_jwt
from enum import Enum

class UserRole(Enum):
    USER="User"
    ADMIN="Administrator"



class User(Base):
    __tablename__ = 'users'
    id = Column('id', Integer, primary_key=True)
    username = Column('username', String(256), unique=True)
    email = Column('email', String(256), unique=True)
    password = Column('password', String(256))
    createdAt = Column('createdAt', DateTime(timezone=True), default=func.now(), nullable=False)
    role = Column('role', SQLEnum(UserRole), nullable=False)
    status = Column('status', Boolean)

    def __init__(self, username, email, password, status=True):
        self.username = username
        self.email = email
        self.password = password
        self.status = status
        self.role = UserRole.USER
    

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'createdAt': self.createdAt.isoformat(),
            'status': self.status,
            'role': self.role.value
        }
    

def get_all_users():
    session = session_factory() # Instancio uma sessao nova com o banco de dados
    try:
        user_orm: User = session.query(User).all() # Uso a sessao criada anteriormente para realizar operações
        if user_orm :
            return True, { 'items': [user.to_json() for user in user_orm] }
        else:
            return False, {'message': 'no user found'}
        
    except Exception as e:
        print('Error', e)
        return {'error': e}
    
    finally:
        session.close()


def get_user_with_id(id):
    session = session_factory()
    try:
        user_orm : User = session.query(User).filter_by(id=id).first()
        if user_orm :
            return True, user_orm.to_json()
        else: 
            return False, {"message": "User not found"}
        
    except Exception as e:
        print('Error', e)
        return False, {'error': e}

    finally:
        session.close()

def get_user_with_email(email):
    session = session_factory()
    try:
        user_orm : User = session.query(User).filter_by(email=email).first()
        if user_orm :
            return user_orm.to_json()
        else: 
            return {"message": "User not found"}
        
    except Exception as e:
        print('Error', e)
        return {'error': f'{e}'}
    
    finally:
        session.close()


def register_user(request):
    session = session_factory()

    user_data = request.get_json()
    username = user_data.get("username")
    email = user_data.get("email")
    password = hash(user_data.get("password"))

    try:
        user = User(username, email, password)
        session.add(user)
        session.commit()
        return True, user.to_json()
    
    except Exception as e:
        print('Error', e)
        session.rollback()
        return False, {"error": e}
    
    finally:
        session.close()

def auth_user(request):
    session = session_factory()
    user_data = request.get_json()
    email = user_data.get("email")
    password = hash(user_data.get("password"))
    try:
        user_orm : User = session.query(User).filter_by(email=email).first()

        if user_orm:
            if user_orm.password == password:
                return True, {"token": f"{create_jwt_token(user_orm)}"}
            else:
                return False, {"message": "Email or password is Incorrect"}
        else:
            return False, {"message": "Email or password is Incorrect"}

    except Exception as e:
        print('Error', e)
        return False, {"error": e}
    
    finally:
        session.close()

def delete_user(id):
    session = session_factory()
    
    try:
        user_orm : User = session.query(User).filter_by(id=id).first()
        session.delete(user_orm)
        session.commit()
        return True, ''
    
    except Exception as e:
        print('Error deleting user:', e)
        session.rollback()
        return False, {"error": e}
    
    finally:
        session.close()

def update_user(id, request):
    session = session_factory()
    try:
        user_orm : User = session.query(User).filter_by(id=id).first()

        username = request.json.get('username')
        email = request.json.get('email')
        password = request.json.get('password')

        if username:
            user_orm.username = username
        if email:
            user_orm.email = email
        if password:
            user_orm.password = hash(password)

        session.commit()
        return True, user_orm.to_json()

    except Exception as e:
        print('Error', e)
        session.rollback()
        return False, {'error': e}

    finally:
        session.close()