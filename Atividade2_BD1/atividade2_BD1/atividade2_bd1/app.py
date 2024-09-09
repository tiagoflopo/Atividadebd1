from fastapi import FastAPI

from http import HTTPStatus

from atividade2_bd1.schema import UserID, UserInfos, UserList, UserPublic


app = FastAPI(
    title='Atividade 2 BD1 - Tiago Ferreira Lopo',
    description=(
        'Aqui temos 3 funções, uma para realizar um cadastro simples de usuário. '
        'Podemos realizar a leitura de todos os usuários do BD,'
        'e também podemos realizar a consulta de um usuário específico através do seu ID.'
    ),
)

database = []

@app.post(
    'Criar Usuário',
    status_code=HTTPStatus.CREATED,
    response_model=UserPublic,
    tags=['Cadastro de Usuário'],
)
def create_user(user: UserInfos):
    db_user = UserID(
        id=len(database) + 1,
        **user.model_dump(),
    )

    database.append(db_user)

    return db_user

@app.get(
    'Ler todos os usuários',
    status_code=HTTPStatus.OK,
    response_model=UserList,
    tags=['Cadastro de Usuário'],
)
def read_users():
    return {'users': database}


@app.get(
    'Ler usuário pelo ID',
    status_code=HTTPStatus.OK,
    response_model=UserPublic,
    tags=['Cadastro de Usuário'],
)
def read_user(user_id: int):
    if user_id > 0 and user_id <= len(database):
        db_user = database[user_id - 1]

        return db_user
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )