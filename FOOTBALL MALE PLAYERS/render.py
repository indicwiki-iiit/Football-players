import pickle
from jinja2 import Environment, FileSystemLoader

# from anuvaad import Anuvaad
# telugu = Anuvaad('english-telugu')
from genXML import tewiki,writepage

from google_trans_new import google_translator
translator=google_translator()

from deeptranslit import DeepTranslit
trans = DeepTranslit('telugu').transliterate

def getData(row):
	# Translation and Transliteration
	d=[]
	l=[]
	y=[]
	p=[]
	#transliteration for tags
	for i in [row.tags]:
		x=i.values[0]
		if x!='nan': 	
			deep=trans(x)[0]
			l.append(deep['pred'])
		else:
			l.append("nan")
	m=",".join(l)
	#transliteration for traits
	for i in [row.traits]:
		x=i.values[0]
		if x!="nan":
			deep=trans(x)[0]
			y.append(deep['pred'])
		else:
			y.append("nan")
	r=",".join(y)
	#transliteration for age and coach
	for i in [row.age_and_coach1]:
		try:
			if i.values[0]!='nan':
				x=eval(i.values[0])
				deep=trans(x[0])[0]
				p.append(deep['pred'])
				deep=trans(x[1])[0]
				p.append(deep['pred'])
				deep=trans(x[2])[0]
				p.append(deep['pred'])
				deep=trans(x[3])[0]
				p.append(deep['pred'])
			else:
				p=["nan","nan","nan","nan"]
		except:
			p=["nan","nan","nan","nan"]

			
	#transliterating attributes using deeptrans
	for i in [row.birth_place,row.club_team,row.full_name,row.nationalty,row.positions,row.name,row.player_awards,
	row.national_team_position,row.N_N,row.club_position,row.tags,row.traits,row.national_career,row['Career Stats'],
	row.debuts,row.age_and_coach1]:
		x=(i.values[0])
		if x!='nan':
			deep=trans(x)[0]
			d.append(deep['pred']) 
		else:
			d.append("nan")

	# Data dictionary 
	data = {
		'birth_place':d[0],
		'club':d[1],
		"n":d[8],
		'full_name':d[2],
		'nationality':row.nationalty.values[0],
		'national_team_position':d[7],
		'team': d[3],
		'long_name':d[2],
		'positions':d[4],
		'c_positions':d[9],
		'player_positions':d[4],
		'short_name':d[5],
		's_name':d[5],
		'tags':m,
		'age_at_debut':p[3],
		'coach_at_debut':p[2],
		'debut_club':p[0],
		"year":p[1],
		"N_N":row.N_Ne.values[0],
		'id': row.id.values[0],
		'player_traits':r,
		'i_r':row.international_reputation.values[0],
		'dob':row.birth_date.values[0],
		'height_cm':row.height_cm.values[0],
		'weight_kg': row.weight_kgs.values[0],
		'w_f':row.weak_foot.values[0],
		
		'r_c':row.release_clause_euro.values[0],
		'team_jersey_num':row.club_jersey_number.values[0],
		
		'img':row.img.values[0],
		'club_joined': row.club_join_date.values[0],
		
		'preferred_foot':row.preferred_foot.values[0],

		'contract_valid_until':row.contract_end_year.values[0],
		
		'potential':row.potential.values[0],
		'overall_rating':row.overall_rating.values[0],
		
		'highest_market_value':row.highest_market_value1.values[0],
		'wage_euro':str(row.wage_euro.values[0]),

		'skill_moves':row.skill_moves.values[0],
		'body_type':row.bodytype.values[0],
		
		
		'ball_control':row.ball_control.values[0],
		'dribbling':row.dribbling.values[0],

		'marking':row.marking.values[0],
		'slide_tackle':row.sliding_tackle.values[0],
		'stand_tackle':row.standing_tackle.values[0],
		'aggression': row.aggression.values[0],
		'reactions':row.reactions.values[0],
		'interception':row.interceptions.values[0],

		'vision':row.vision.values[0],
		'composure':row.composure.values[0],
		'acceleration':row.acceleration.values[0],
		'strength': row.strength.values[0],
		'balance':row.balance.values[0],
		'stamina':row.stamina.values[0],
		'sprint_speed':row.sprint_speed.values[0],

		'agility':row.agility.values[0],
		'jumping':row.jumping.values[0]
		

		
	}
	#reading 2d list attributes into data dictionary
	A=row.national_jersey_number.values[0]
	if A!='nan':
		data['m_jersey_num']=int(float(A))
	else:
		data['m_jersey_num']='nan'

	if d[6]=='nan':
		data['awards']='nan'
	else:
		data['awards']=eval(d[6])
		l=len(eval(d[6]))
		l_list=list(range(l,l+1))
		data['l_list']=l_list

	if d[12]=='nan':
		data['national_career']='nan'
		
	else:
		data['national_career']=eval(d[12])

	if d[13]=='nan':
		data['stats']='nan'
	else:
		data['stats']=eval(d[13])
	if d[14]=='nan':
		data['debut']='nan' 
	else:
		data['debut']=eval(d[14])
	
	return data


def main():
	#reading jinja2 template
	file_loader = FileSystemLoader(r'C:\Users\hp\Desktop\indicwiki\ToyProject\template')
	env = Environment(loader=file_loader)
	template = env.get_template('playerstemplate.j2')
	#generating pickle file
	playerDF =pickle.load(open(r'C:\Users\hp\Desktop\indicwiki\ToyProject\data\playerDF.pkl', 'rb'))

	ids = playerDF.id.tolist()
	ids =ids[0:1] 
	# Initiate the file object
	fobj = open('footballplayersXML.xml','w',encoding='utf-8')
	fobj.write(tewiki)
	fobj.write('\n')
	#rendering article for each player
	for i, playerId in enumerate(ids):
		row = playerDF.loc[playerDF['id']==playerId]
		playername = row.N_N.values[0]
		text = template.render(getData(row))

		writepage(playername, text, fobj)		

		print(i, playername)
		print(text, '\n')
	#writing article 
	fobj.write('</mediawiki>')
	fobj.close()

if __name__ == '__main__':
	main()
