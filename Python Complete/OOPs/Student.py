class father:
    def skill(self):
        print("Father's skill is gaurdening")
class mother:
    def skill2(self):
        print("Mother's skill is cooking")
class son(father, mother):
    def skill3(self):
        print("Son skill is sports")
s = son()
s.skill2()    