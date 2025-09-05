import pyinputplus as pyip

def addFunc(add,totalCost,addFunc):
        addingsChoice=pyip.inputMenu(list(addings.keys()),numbered=True,prompt='どれにしますか?\n')
        totalCost+=addings[addingsChoice]
        del addings[addingsChoice]
        if len(addings)>1:
            add=pyip.inputYesNo(prompt='もうひとつ追加しますか?\n')
            if add=='yes' or add=='Y' or add=='YES' or add=='Yes':
                addFunc(add,totalCost,addFunc)

totalCost=0
breadType={'小麦パン': 150,'白パン':200,'サワー種':200}
proteinType={'チキン':150,'ターキー':200,'ハム':220,'豆腐':170}
cheezType={'チェダー':100,'スイス':150,'モツァレラ':200}
addings = {'マヨネーズ': 50, 'からし': 50, 'レタス': 100, 'トマト': 100}

breadChoice=pyip.inputMenu(list(breadType.keys()),numbered=True, prompt='どのようなパンがお好みですか?\n')
totalCost+=breadType[breadChoice]

print()
proteinChoice=pyip.inputMenu(list(proteinType.keys()),numbered=True,prompt='具材は何にしますか?\n')
totalCost+=proteinType[proteinChoice]

print()
cheese=pyip.inputYesNo(prompt='チーズをのせますか?\n')
if cheese=='yes':
    cheeseChoice=pyip.inputMenu(list(cheezType.keys()),numbered=True,prompt='チーズは何にしますか?\n')
    totalCost+=cheezType[cheeseChoice]

print()
add=pyip.inputYesNo(prompt='マヨネーズ、レタス、マスタード、トマトを追加しますか?\n')
if add=='yes':
    addFunc(add,totalCost,addFunc)

print()
numOfSandwich=pyip.inputNum(prompt="このサンドイッチを何個ご注文になりますか?\n",min=1)
totalCost*=numOfSandwich

print('--->お会計は'+str(totalCost)+'円になります。 ありがとうございました！')
