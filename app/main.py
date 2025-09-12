from fastapi import FastAPI, Depends, HTTPException
from app.config.db import Base,engine, get_db
from sqlalchemy.orm import Session
from app.models.game import Game
from app.schemas.gameschema import GameSchema
app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/game")
def getdata(db: Session = Depends(get_db)):
    return db.query(Game).all()

@app.post("/game")
def add_game( body : GameSchema, db: Session = Depends(get_db)):
    game = Game(name=body.name,type=body.type)
    db.add(game)
    db.commit()
    db.refresh(game)
    return game

@app.get("/game/{id}")
def getgamebyid(id: int,db: Session = Depends(get_db)):
    return db.query(Game).filter_by(id=id).all()

@app.delete("/game/{id}")
def deletegame(id:int, db: Session = Depends(get_db)):
    game = db.query(Game).filter_by(id=id).first()
    if game:
        db.delete(game)
        db.commit()
        return "Game deleted successfully"
    else:
        raise HTTPException(status_code=404,detail="game does not exists")
