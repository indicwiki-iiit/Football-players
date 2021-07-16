from jinja2 import Environment,FileSystemLoader
import pickle

from genXML1 import tewiki, writepage

# Google trans new libary for Translation
from google_trans_new import google_translator
translator = google_translator()

# deeptranslit for Transliteration
from deeptranslit import DeepTranslit
translit = DeepTranslit('telugu').transliterate

def getdata(row):
    global translit

    # Data dictionary
    data = {
            # {%- macro infobox()-%}
            # {%- macro intro(name,tname,dob1,age,nation,positions,preferred_foot,work_rate,kit_no) -%}
            # {%- macro personal_life(name,birth_place,dob) -%}
            'id':row.sid.values[0],
            'name':row.Name.values[0],
            'img':row.url.values[0],
            'tname':row.tname.values[0],
            'heading':row.heading.values[0],
            'position1':row.tposition1.values[0],
            'positions1':row.tpositions1.values[0],
            'nation':row.tnation.values[0],
            'dob':row.dob.values[0],
            'dob1':row.tdob.values[0],
            'age':row.age.values[0],
            'kit_no':row.kit_no.values[0],
            'height':row.Height.values[0],
            'weight':row.Weight.values[0],
            'preferred_foot':row.tpreferred_foot.values[0],

            # {%- macro ballskills(name,ball_control,dribbling) -%}
            'ball_control':row.ball_control.values[0],
            'dribbling':row.driblling.values[0],

            # {%- macro defence(marking,slide_tackle,stand_tackle) -%}
            'marking':row.marking.values[0],
            'stand_tackle':row.stand_tackle.values[0],
            'slide_tackle':row.slide_tackle.values[0],

            # {%- macro shooting(name, heading, shot_power, finishing, long_shots, curve, fk_acc, Penalties, Volleys) -%}
            'crossing':row.crossing.values[0],
            'att_postiton':row.att_position.values[0],
            'finishing':row.finishing.values[0],
            'short_pass':row.short_pass.values[0],
            'volleys':row.volleys.values[0],
            'shot_power':row.shot_power.values[0],
            'curve':row.curve.values[0],
            'fk_acc':row.fk_acc.values[0],
            'long_pass':row.long_pass.values[0],
            
            # {%- macro physical(name,acceleration,stamina,strength,balance,sprint_speed,agility,jumping) -%}
            'acceleration':row.acceleration.values[0],
            'sprint_speed':row.sprint_speed.values[0],
            'agility':row.agility.values[0],
            'balance':row.balance.values[0],
            'jumping':row.jumping.values[0],
            'stamina':row.stamina.values[0],
            'strength':row.strength.values[0],
            'penalties':row.penalities.values[0],
            'long_shots':row.long_shots.values[0],

            # {%- macro mentalstate(name,aggression,reactions,interception,vision,composure) -%}
            'aggression':row.agression.values[0],
            'interception':row.Interception.values[0],
            'vision':row.vision.values[0],
            'composure':row.composure.values[0],
            'reaction':row.reactions.values[0],
            
            # {%- macro goalkeeping(name,GK_Positioning,GK_Diving,GK_Handling,GK_Kicking,GK_Reflexes)%}

            'GK_diving':row.GK_Diving.values[0],
            'GK_handling':row.GK_Handling.values[0],
            'GK_kicking':row.GK_Kicking.values[0],
            'GK_positioning':row.GK_Positioning.values[0],
            'GK_reflexes':row.GK_Reflexes.values[0]
        }

    return data

def main():
    file_loader = FileSystemLoader('./template')
    env = Environment(loader = file_loader)
    template = env.get_template('./female players.j2')

    footballDF = pickle.load(open('./female_players/female_plyrsDF.pkl','rb'))

    ids = footballDF.sid.tolist()

    # Initialize the file object
    fobj = open('femaleplayersXML1.xml','w',encoding='utf-8')
    fobj.write(tewiki)
    fobj.write('\n')

    for i,fid in enumerate(ids):
        row = footballDF.loc[footballDF['sid']==fid]
        title = row.tname.values[0]
        text = template.render(getdata(row))
        
        writepage(title,text,fobj)

        print('\n',i,title)
        print(text,'\n')
        
    fobj.write('</mediawiki>')
    fobj.close()
    
if __name__ =='__main__':
    main()
