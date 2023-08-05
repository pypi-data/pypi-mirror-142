# 22-3-11  dsk into one redis-db,  mkf:{snt}, fd:{snt}, bs:{snt},  eidv, rid:{rid}, uid:{uid}
import json, sys, time, redis, fire,traceback, spacy,requests

if not hasattr(spacy, 'nlp'): 
	spacy.nlp		= spacy.load('en_core_web_sm')
	spacy.frombs	= lambda bs: list(spacy.tokens.DocBin().from_bytes(bs).get_docs(spacy.nlp.vocab))[0] if bs else None
	spacy.tobs		= lambda doc: ( doc_bin:= spacy.tokens.DocBin(), doc_bin.add(doc), doc_bin.to_bytes())[-1]
	spacy.getdoc	= lambda snt: ( bs := redis.bs.get(f"bs:{snt}"), doc := spacy.frombs(bs) if bs else spacy.nlp(snt), redis.bs.setnx(f"bs:{snt}", spacy.tobs(doc)) if not bs else None )[1]

def hver(key, eid, ver ):
	res = redis.r.hget(key, eid)
	try: 
		if not res :
			redis.r.hset(key, eid, ver)
		else: 
			if int(ver) > int(res) : redis.r.hset(key, eid, ver)
	except Exception as e:
		print("ex:", e, eid)

def submit_hdsk(dsk, rid, uid, eid, ver):
	''' added 2021.12.9 '''
	try: 
		info = dsk.get('info',{})
		eidv = f"{eid}-{ver}"
		score = info.get('final_score', 0)

		redis.r.zadd("eids",  { f"{eid}-{ver}":  int(eid) + min(int(ver)/100000, 0.99) })	
		redis.r.zadd(eid,  {ver: int(ver) })	
		hver(f"rid:{rid}", eid, ver ) 
		hver(f"uid:{uid}", eid, ver ) 
		redis.r.sadd("rids",  rid)	
		redis.r.sadd("uids",  uid)	

		redis.r.hset(eidv, 'rid', rid, {'uid':uid, 'score': score, 
		'snts': json.dumps([arrsnt['meta'].get('snt','').strip() for arrsnt in dsk['snt'] ]), 
		"pids": json.dumps([arrsnt['meta'].get('pid',-1) for arrsnt in dsk['snt'] ]),
		"dim":	json.dumps(dsk['doc']), 
		"kw":	json.dumps(dsk['kw']), 
		"info": json.dumps(dsk['info']), 
		})

		for arrsnt in dsk['snt']:
			snt = arrsnt.get('meta',{}).get('snt','')
			spacy.getdoc(snt)
			redis.r.setnx( f"mkf:{snt}", json.dumps(arrsnt))
			for k, v in arrsnt.get('feedback',{}).items():
				cate = v.get('cate','')
				if cate.startswith ("e_") or cate.startswith("w_"): 
					redis.r.hset(f"fd:{snt}", cate, v.get('kp',''))
	
	except Exception as e:
		print("ex:", e, dsk)
		exc_type, exc_value, exc_obj = sys.exc_info()
		traceback.print_tb(exc_obj)

class util(object):
	def __init__(self, host='127.0.0.1', port=6379, db=0):
		redis.r	 = redis.Redis(host=host, port=port, db=0, decode_responses=True)
		redis.bs = redis.Redis(host=host, port=port, db=0, decode_responses=False)

	def test(self): 
		arr = {"key":"1002-3", "rid":"10", "essay":"English is a internationaly language which becomes importantly for modern world. In China, English is took to be a foreigh language which many student choosed to learn. They begin to studying English at a early age. They use at least one hour to learn English knowledges a day. Even kids in kindergarten have begun learning simple words. That's a good phenomenan, for English is essential nowadays. In addition to, some people think English is superior than Chinese. In me opinion, though English is for great significance, but English is after all a foreign language. it is hard for people to see eye to eye. English do help us read English original works, but Chinese helps us learn a true China. Only by characters Chinese literature can send off its brilliance. Learning a country's culture, especial its classic culture, the first thing is learn its language. Because of we are Chinese, why do we give up our mother tongue and learn our owne culture through a foreign language?"}
		dsk = requests.post("http://wrask.com:7002/gec/dsk?dskhost=dsk.jukuu.com", json=arr).json() 
		submit_hdsk(dsk, 10, 101, 1001,3 ) 

	def load(self, infile): 
		''' load eev dumped file, one line, one json  '''
		from util import readline 
		print ("start to load:", infile, flush=True) 
		for line in readline(infile): 
			try:
				arr = json.loads(line.strip().replace(", null,", ", '',") )
				dsk = requests.post("http://wrask.com:7002/gec/dsk?dskhost=dsk.jukuu.com", json={"essay": arr.get('essay','')}).json()
				submit_hdsk(dsk, arr.get('request_id',0), arr.get("user_id",0), arr.get('essay_id',0), arr.get('version',0) ) 
			except Exception as e:
				print("ex:", e, line)

if __name__ == '__main__': 
	fire.Fire(util) 

'''
rport = 6379
redis.r	 = redis.Redis(host='127.0.0.1', port=rport, db=0, decode_responses=True)
redis.bs = redis.Redis(host='127.0.0.1', port=rport, db=0, decode_responses=False)
'''