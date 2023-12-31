import sys,csv,time

  
def pass1(baskets,s,N):
    items={}
    hasht={}
    
    for b in baskets:
      for i in range(len(b)):
        if b[i] not in items:
          items[b[i]]=1
        else:
          items[b[i]]+=1
        for j in range(i+1,len(b)):
          pair=(b[i],b[j])
          bucket=hash(pair)%N
          #bucket=int(b[i]+b[j])%N
          if bucket not in hasht:
            hasht[bucket]=1
          elif hasht[bucket]<s:
            hasht[bucket]+=1
    '''
    for b in baskets:
      for i in b:
        if i not in items:
          items[i]=1
        else:
          items[i]+=1
    print('C1:',len(items))
    for b in baskets:
      for i in range(len(b)-1):
        for j in range(i+1,len(b)):
          pair=(b[i],b[j])
          bucket=hash(pair)%N
          #bucket=int(b[i]+b[j])%N
          if bucket in hasht:
            hasht[bucket]+=1
          else:
            hasht[bucket]=1
    '''
    #print('Hash Table:',len(items))
    rest=[i for i in hasht if hasht[i]>=s]
    #print('More Than S:',len(rest))
    
    frequent_items=[(i,) for i in items if items[i] >= s]
    #print('L1:',len(frequent_items))
    return frequent_items,hasht

  
def pass2(ffc,baskets,s,vector,N):
    candidates={}
    for i in range(len(ffc)-1):
        for j in range(i+1,len(ffc)):
          pair=ffc[i]+ffc[j]
          h=hash(pair)%N
          if h in vector:
            candidates[pair]=0
    #print('C'+str(2)+':',len(candidates))
    
    for b in baskets:
        for c in candidates:
          if c[1] in b and c[0] in b:
            candidates[c]+=1

    freq_candidates=[i for i in candidates if candidates[i]>=s]
    #print('L'+str(2)+':',len(freq_candidates))
    return freq_candidates
  
  
#ffc=former frequent candidates
#s=support
#K=the size of frequent items that will return 
def passk(K,ffc,baskets,s):
    assert(K>1),'Can Not Use Passk() At First Pass'
    def all_in_former(merged,ffc):
        sub={}
        merged=list(merged)
        for i in merged:
          temp=[i for i in merged]
          temp.remove(i)
          sub[tuple(temp)]=False  
        for c in ffc:
          for s in sub:
            if set(c)==set(s):
              sub[s]=True
        all_in=True
        for s in sub:
          if sub[s]==False:
            all_in=False   
        return all_in
      
    def not_duplicate(merged,candidates):
        not_in=True
        for t in candidates:
            if set(t)==set(merged):
                not_in=False
        return not_in
    
    candidates={}
    
    for i in range(len(ffc)-1):
        for j in range(i+1,len(ffc)):
            merged=tuple(set(ffc[i]+ffc[j]))
            if len(merged)==K:
                if not_duplicate(merged,candidates):
                    if all_in_former(merged,ffc):
                        candidates[merged]=0
    print('C'+str(K)+':',len(candidates))
                       
    check=[]
    t=list(candidates)
    for i in range(len(t)-1):
        for j in range(i+1,len(t)):
            if set(t[i]) == set(t[j]):
                check.append(t[j])
    assert(len(check)==0),'Exist Duplicate Candidate Elements'
    
    for b in baskets:
        for c in candidates:
            all_in_basket=True
            for i in c:
                if i not in b:
                    all_in_basket=False
                    break
            if all_in_basket:
                candidates[c]+=1
        
    freq_candidates=[i for i in candidates if candidates[i]>=s]
    #print('L'+str(K)+':',len(freq_candidates))
    return freq_candidates
  
  
def pcy(data,K,sup_rate,N):
  #start = time.clock()
  
  baskets=data
  #del baskets[0]
  #print('Data:',len(baskets))
  support=sup_rate*len(baskets)
  #print('Support:',support)
  
  singleton,hasht=pass1(baskets,support,N)
  
  for i in hasht:
    if hasht[i]>=support:
      hasht[i]=1
    else:
      hasht[i]=0
  vector=[i for i in hasht if hasht[i]==1]
  
  freq_items=singleton
  for i in range(2,K+1):
    if i==2:
        freq_items=pass2(freq_items,baskets,support,vector,N)
    else:
        freq_items=passk(i,freq_items,baskets,support)
  
  #print ('Run Time:',time.clock()-start)
  return freq_items