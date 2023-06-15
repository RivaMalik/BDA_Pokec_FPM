def categorizedEducationLevels(column):
    categorized_edu_list=[]
    for val in column:
      temp=val.split()
      
      if  set(temp).intersection(["zakladne","skole","skolka"]) !=set():
        categorized_edu_list.append("zakladne")

      elif  set(temp).intersection(["stredoskolske","strednej","stredna","stredne"]) !=set(): 
        categorized_edu_list.append("stredoskolske")

      elif  set(temp).intersection(["vysokoskolske","bakalarske"]) !=set():
        categorized_edu_list.append("vysokoskolske")

      elif  set(temp).intersection(["ucnovske"]) !=set(): 
        categorized_edu_list.append("ucnovske")

      else:
        categorized_edu_list.append("")

    return categorized_edu_list

