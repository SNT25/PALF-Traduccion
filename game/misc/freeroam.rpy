label freeroam:

python:
    location = "school"
    AddPikachu()
    HealParty() 

label beforemusic:

stop music fadeout 2.5

$ renpy.music.queue("audio/music/GSCBike_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
$ renpy.music.queue("audio/music/GSCBike_Loop.ogg", channel='music', loop=True)
$ freeroaming = True

scene map with splitfade
show blank2 as blackground behind map
show screen currentdate 
call screen map_UI(_with_none=False)
hide blackground
with dissolve

jump skipresetup

label aftersetup:
scene map
show screen currentdate
call screen map_UI(_with_none=False)

label skipresetup:

$ trainer1 = Trainer("red", TrainerType.Ally, playerparty)

$ interaction = _return
if (interaction in GetStudents()):
    $ interactionsprite = GetCharacterSprite(interaction)

if (interaction == "Study"):
    redmind @thinking "¿En que tipo debería enfocarme?"

    show blank2 with dis:
        alpha 0.8

    $ lastclass = ""

    call screen studyfocus
    $ selectedtype = _return 

    hide blank2 with dis

    if (selectedtype == "Back"):
        jump aftersetup

    if (excusesecondelective or excusesecondhomeroom):
        redmind uniform @thinking "Casi todos los demás están en clase ahora mismo, así que tendré que estudiar solo. No creo sea tan efectivo como estudiar con alguien."

        menu:
            "Esta bien.":
                $ IncreaseProficiency(selectedtype, 0.25)

            "Mejor no estudio.":
                jump aftersetup
    else:
        $ willstudy = list(WillStudy(selectedtype))
        if (len(willstudy) > 0):
            $ randomstudent = RandomChoice(list(WillStudy(selectedtype)), True)

            $ pronoun = ("él" if persondex[randomstudent]["Sex"] == Genders.Male else "ella")

            label afterlibraryseed:

            redmind @thinking "Parece que [randomstudent] está en la biblioteca. ¿Debería estudiar con [pronoun]?"

            menu: 
                "Seguro, ¿por que no?":
                    show library with Dissolve(1.0)
                    $ imagestring = GetCharacterSprite(randomstudent)
                    $ renpy.show(imagestring, [dissolvein])

                    pause 1.0

                    narrator "Pasaste algo de tiempo estudiando Pokémons de tipo [selectedtype] con [randomstudent]."

                    python:
                        renpy.show(GetCharacterSprite(randomstudent, 10))
                        if (randomstudent in ["Jasmine", "Grusha"]):
                            ValueChange(randomstudent, 4, 0.5)
                        else:
                            ValueChange(randomstudent, 2, 0.5)

                        IncreaseProficiency(selectedtype, 0.5)

                        renpy.transition(dis)
                        renpy.hide(imagestring)

                "Mejor llamo a alguien más.":
                    redmind @thinking "Muy bien... veamos si a alguien le interesa estudiar esto conmigo."
                    redmind @thinking "Tengo que tener en cuenta si estudian esa electividad, sino no creo que podamos estudiar juntos."

                    show phone_B 
                    show phone_A
                    with fadeinbottom

                    hide blank2 with dis

                    call screen database(calling=True, limittype=selectedtype, _with_none=False) with Dissolve(1.0)
                    with dissolve
                    $ contact = _return

                    if (contact == "Back"):
                        hide phone_B 
                        hide phone_A
                        with fadeoutbottom
                        jump afterlibraryseed
                    elif (contact != "Sabrina"):
                        $ pronoun = ("he" if persondex[contact]["Sex"] == Genders.Male else "she")
                        redmind @thinking "Ok, le mandare un mensaje a [contact] y vere si [pronoun] puede venir."
                    else:
                        hide phone_B 
                        hide phone_A
                        with fadeoutbottom
                        redmind @thinking "Ok, pensare muy fuerte en Sabrina y vere si ella viene."

                    if (contact.title() not in WillStudy(selectedtype)):
                        pause 3.0

                        narrator "No hubo respuesta..."

                        jump aftersetup

                    show library with Dissolve(1.0)

                    hide phone_B 
                    hide phone_A
                    with fadeoutbottom

                    $ renpy.show(GetCharacterSprite(contact, 0), [dissolvein])

                    pause 1.0

                    narrator "Pasaste algo de tiempo estudiando Pokémons de tipo [selectedtype] con [contact]."

                    $ renpy.transition(dis)
                    $ renpy.show(GetCharacterSprite(contact, 10))
                    $ ValueChange(contact, 1, 0.5)
                    $ IncreaseProficiency(selectedtype, 0.5)

                    $ renpy.transition(dis)
                    $ renpy.hide(contact.lower())
                
                "Pensandolo bien, no quiero estudiar.":
                    jump aftersetup
        
        else:
            redmind uniform @thinking "Parece que no hay nadie en la biblioteca ahora mismo, así que tendré que estudiar solo. No creo sea tan efectivo como estudiar con alguien."

            menu:
                "Esta bien.":
                    $ IncreaseProficiency(selectedtype, 0.25)

                "Mejor no estudio.":
                    jump aftersetup

elif (interaction == "Town"):
    if (IsBefore(17, 4, 2004)):
        redmind @thinking "Creo que debería acostumbrarme un poco más a estar en el campus antes de salir solo."
        jump aftersetup

    elif (trainer1.HasMons()):
        menu:
            "Ir a la ciudad.":
                call city from _call_city

            "Mejor no.":
                jump aftersetup
    else:
        redmind @thinking "No debería salir del campus con un equipo tan cansado."
        jump aftersetup

elif (interaction == "Fields"):
    if (IsBefore(13, 4, 2004)):
        redmind @thinking "Creo que debería acostumbrarme un poco más a estar en el campus antes de salir solo."
        jump aftersetup

    elif (IsAfter(10, 5, 2004) and not (rescuedwill and rescuedsabrina and rescuedtia) and IsBefore(17, 5, 2004)):
        menu:
            "{color=#0f0}[[Easy]{/color} >Rescatar al Prof. Mento de la Senda Marchita." if not rescuedwill:
                jump unhallowedholt

            "{color=#00f}[[Medium]{/color} >Rescatar a Tia del Claro Quebrado." if not rescuedtia:
                jump shatteredglades

            "{color=#f00}[[Hard]{/color} >Rescatar a Sabrina de los Arboles Susurrantes." if not rescuedsabrina:
                jump windsweptwoods
 
            ">Ir a los campos":
                if (trainer1.HasMons()):
                    $ wildcount = 0
                    call wildarea("fields") from _call_wildarea_1
                else:
                    redmind @thinking "No debería salir del campus con un equipo tan cansado."
                    jump aftersetup

            ">Salír":
                jump aftersetup

    elif (trainer1.HasMons()):
        $ wildcount = 0

        if (IsDate(17, 5, 2004)):
            call cyclizarhunt from _call_cyclizarhunt

        if (IsBefore(18, 5, 2004)):
            call wildarea("fields") from _call_wildarea

        else:
            menu:
                ">Ir a los campos":
                    call wildarea("fields") from _call_wildarea_5

                ">Ir a la Montaña Argéntea":
                    python:
                        rideable = None
                        for mon in playerparty:
                            if (pokedexlookupname("Cyclizar", DexMacros.Id) == mon.Id):
                                rideable = mon
                                break
                    if (rideable == None):
                        narrator "¿Te gustaría pagar $200 para alquilar un Cyclizar y subir a la cumbre?"

                        menu:
                            ">Pagar":
                                if (money < 200):
                                    narrator "Vergonzosamente, no tienes suficiente para pagar la tarifa..."
                                
                                    jump aftersetup

                                else:
                                    $ money -= 200

                                    scene blank2 with splitfade

                                    narrator "Montas en el Cyclizar alquilado hasta la Montaña Argéntea."

                                    $ sidemonnum = pokedexlookupname("Cyclizar", DexMacros.Id)
                                    $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
                                    sidemon "¡Cyc! ¡Lizar!"

                            ">Mejor no":
                                jump aftersetup

                    else:
                        scene blank2 with splitfade

                        if (GetRelationshipRank("Silver") > 1):
                            narrator "Te pones el equipo para la nieve que Silver te dio y montas tu Cyclizar hasta la Montaña Argéntea."
                        else:
                            narrator "Montas en el Cyclizar alquilado hasta la Montaña Argéntea."

                        $ sidemonnum = pokedexlookup("Cyclizar", DexMacros.Id)
                        $ cyclizarnickname = rideable.GetNickname()
                        $ PlaySound("pokemon/cries/{}.mp3".format(sidemonnum))
                        $ sidemonoverride = cyclizarnickname
                        sidemon "¡Cyc! ¡Lizar!"
                        $ sidemonoverride = None

                    call wildarea("mountain") from _call_wildarea_6

                "Mejor no.":
                    jump aftersetup
    else:
        redmind @thinking "No debería salir del campus con un equipo tan cansado."
        jump aftersetup 

elif (interaction == "Business"):
    show baseball
    show gardenia 
    with dis
    gardenia @happy "¡Hola! Te ves genial. ¿Listo para hablar de negocios?"
    $ baseindex = investmentthresholds.index(highestbank)
    label beginbusiness:

    if (highestbank < GetNextInvestmentThreshold()):
        $ highestbank = GetNextInvestmentThreshold()
        gardenia @surprised "¡Vaya, acabas de alcanzar una nueva meta!" 
        $ ValueChange("Gardenia", investmentthresholds.index(highestbank) - baseindex)
        gardenia @happy "Como agradecimiento por hacer negocios con nosotros (conmigo), hemos (he) aprobado un incremento en la tasa de interés de tu cuenta."
        gardenia @talkingmouth "A partir de ahora, puedes esperar ganar un agradable y redondo $[math.floor(highestbank / 100)] todos los días hasta que termine el año."
        gardenia @happy "¡Estoy deseando tener muchos más encuentros sobre negocios, mi queridísimo amigo de los negocios!"

        if (not HasEvent("Gardenia", "FirstThresholdPassed")):
            $ AddEvent("Gardenia", "FirstThresholdPassed")
            red @sadbrow talkingmouth "Uh... sí... no puedo evitar pensar que, por mucho que ahorre, siempre serán unas piedritas comparado con tu imperio financiero."

            gardenia @talkingmouth "Tal vez sean solo piedritas, pero, oye, ¿sabes cuántas hacen falta para {i}cepultar{/i} un imperio?"

            red @confused "Ehm, ¿cuántas?"

            gardenia @sadbrow talkingmouth "Cero. Preguntale a un Paldeano."

            red @closedbrow talking2mouth "Uf, buen punto."

            gardenia @happy "Valoro {i}cada{/i} piedrita que me entregan, por más pequeña que sea. No te preocupes si solo representas una diminuta fracción de mi imperio; lo aprecio de todos modos."

            red @happy "Se siente bien ser apreciado."

    if (highestbank > 0 and not HasEvent("Gardenia", "InvestmentIntro")):
        $ AddEvent("Gardenia", "InvestmentIntro")
        gardenia @surprised "¡Oh, eso me hizo acordar! Dado que mi banco te hace ganar algo de dinero todos los días, pensé en contarte algo en lo que podrías estar interesado en gastarlo."

        red @closedbrow talkingmouth "Típico de Gardenia. Me ofreces un modo de ganar dinero, {i}y{/i} otro para gastarlo."

        gardenia @talking2mouth "Siempre hay que apuntar a expandir el imperio."
        gardenia @talkingmouth "Existen una tonelada de ítems que nunca encontrarás en tiendas gestionadas por la Liga Pokémon." 
        gardenia @talking2mouth "Estoy hablando de ítems como vitaminas que hacen que los entrenamientos de EV sean tan fáciles como respirar, hierbas medicinales más efectivas que superan por mucho a lo que ofrece la Liga..."
        gardenia @happy "También ítems para evolucionar, protectores, garras afiladas, incluso cosas importadas del extranjero, como esas armaduras de Paldea que vuelven locos a los Charcadet."

        red @closedbrow talkingmouth "Aquí hay gato encerrado."

        gardenia @sadbrow talking2mouth "Esto me temo, no vale la pena tanto en tiempo como en dinero para comercializarlos si no hay una demanda." 
        gardenia @talking2mouth "Si inviertes en mis envíos e importaciones, entonces puedo abrir un pequeño mercado aquí llamado la -- 'Tienda de Baratijas'-- la cual venda ese tipo de ítems."

        red @closedbrow talking2mouth "¿Quieres que te pague para que me vendas cosas?"

        gardenia @happy "Dadas las coimas que tendré que dar para sortear los aranceles, ¡no podría pedir mucho más!"

        red @sweat talkingmouth "Debería ser agradecido entonces."

        gardenia @talkingmouth "¡Ya lo vas comprendiendo! [bluecolor]Si quieres que amplíe mi inventario, solo ven aquí, háblame y preguntame sobre invertir dinero en la tienda.{/color} ¡Nunca diré que no!"
    
    menu:
        ">Administrar mi dinero del banco":
            $ previoushighestbank = GetNextInvestmentThreshold()
            gardenia @happy "¡Gracias por ahorrar con nosotros! {w=0.5}... y por 'nosotros' me refiero a 'mí'. Actualmente tienes $[bank] guardados conmigo."
            if (bank == 0):
                gardenia @talking2mouth "¿Por qué no arreglamos esto?"

            $ interest = math.floor(highestbank / 100)
            if (highestbank != 100000):
                $ nextthreshold = investmentthresholds[investmentthresholds.index(highestbank) + 1]
                $ nextinterest = math.floor(nextthreshold / 100)

            if (highestbank not in [0, 100000]):
                gardenia @talkingmouth "Por ahora, estás generando $[interest] diarios en intereses. Esa cifra subirá a [nextinterest] una vez que tu dinero total en el banco llegue a [nextthreshold]."
            elif (highestbank == 0):
                gardenia @talkingmouth "Actualmente no tienes ningun deposito. Si quieres empezar a ganar un poco de dinero todos los días, necesitaré que guardes al menos $1000 aquí."
                gardenia @happy "Tranquilo, en solo cien días recuperarás lo invertido sin problemas."
                gardenia @angrybrow talkingmouth "Aunque podrías depositar, alcanzar la meta para un nuevo tipo de interés y retirar todo tu dinero..."
                gardenia @sadbrow talking2mouth "Pero tal vez no sea buena idea cargar con todo tu dinero. ¿Qué pasaría si pierdes contra un Pokémon salvaje o lo apuestas en una batalla? Podrías correr el riesgo de perder tus preciadas ganancias. Es más seguro dejarlo en mis manos."
                gardenia @happy "De cualquier manera, la decisión es tuya, pero tengo cosas que hacer. ¿Qué piensas hacer?"
            else:
                gardenia @talkingmouth "Ahora mismo estás generando $[interest] diarios en intereses. ¡Ya alcanzaste el límite! Siendo sincera, llevo un tiempo perdiendo dinero contigo... pero hay muchos tipos de inversiones, y creo que tú eres una que vale la pena."

            menu:
                ">Depositar dinero en el banco" if (money > 0):
                    gardenia @talkingmouth "{i}¡Ahora{/i} sí que estamos en negocios! ¿Cuánto quieres depositar?"
                    
                    $ newinvestment = renpy.input("¿Cuanto quieres depositar?", default=money, length=7, allow="1234567890")
                    if (not newinvestment.isdigit()):
                        $ newinvestment = 0
                    else:
                        $ newinvestment = int(newinvestment)

                    if (newinvestment > money):
                        gardenia @angry "Cuidado, amigo. Será mejor que no intentes darme un cheque que será rebotado cuando llegue el momento de cobrarlo."

                        red @sweat closedbrow talking2mouth "Ups, conté mal, déjame ver de nuevo..."

                    elif (newinvestment == 0):
                        pass

                    else:
                        $ money -= newinvestment
                        $ bank += newinvestment

                        gardenia @angrybrow talkingmouth "Has depositado $[newinvestment]; excelente, me encargaré de resguardarlos con mucho recelo..."

                        $ newesthighestbank = GetNextInvestmentThreshold()

                        if (previoushighestbank != newesthighestbank):
                            gardenia @surprised "¡Vaya, acabas de alcanzar una nueva meta!" 
                            $ ValueChange("Gardenia", investmentthresholds.index(newesthighestbank) - baseindex)
                            gardenia @happy "Como agradecimiento por hacer negocios con nosotros (conmigo), hemos (he) aprobado un incremento en la tasa de interés de tu cuenta."
                            gardenia @talkingmouth "A partir de ahora, puedes esperar ganar un agradable y redondo $[math.floor(highestbank / 100)] todos los días hasta que termine el año."
                            gardenia @happy "¡Estoy deseando tener muchos más encuentros sobre negocios, mi queridísimo amigo de los negocios!"

                            if (not HasEvent("Gardenia", "FirstThresholdPassed")):
                                $ AddEvent("Gardenia", "FirstThresholdPassed")
                                red @sadbrow talkingmouth "Uh... sí... no puedo evitar pensar que, por mucho que ahorre, siempre serán unas piedritas comparado con tu imperio financiero."

                                gardenia @talkingmouth "Tal vez sean solo piedritas, pero, oye, ¿sabes cuántas hacen falta para {i}cepultar{/i} un imperio?"

                                red @confused "Ehm, ¿cuántas?"

                                gardenia @sadbrow talkingmouth "Cero. Preguntale a un Paldeano."

                                red @closedbrow talking2mouth "Uf, buen punto."

                                gardenia @happy "Valoro {i}cada{/i} piedrita que me entregan, por más pequeña que sea. No te preocupes si solo representas una diminuta fracción de mi imperio; lo aprecio de todos modos."

                                red @happy "Se siente bien ser apreciado."

                ">Retirar dinero" if (bank > 0):
                    gardenia @sadbrow talkingmouth "Ah... 'Retirar'. Mi palabra menos favorita."
                    $ withdrawal = renpy.input("¿Cuánto  te gustaría retirar?", default=bank, length=7, allow="1234567890")
                    if (not withdrawal.isdigit()):
                        $ withdrawal = 0
                    else:
                        $ withdrawal = int(withdrawal)

                    if (withdrawal > bank):
                        gardenia @happy "Lo siento, mi queridísimo amigo, pero no creo que tengas esa cantidad depositada."
                        gardenia @angrybrow talking2mouth "Me gustaría darte un préstamo, pero te lo digo de antemano: mis tasas de interés son {i}brutales.{/i}"

                        red @sweat happy "Me tientas, me tientas...{w=0.5} Pero mejor paso."
                    
                    elif (withdrawal == 0):
                        pass

                    else:
                        $ money += withdrawal
                        $ bank -= withdrawal

                        gardenia @angrybrow talkingmouth "Aquí están tus $[withdrawal]. {w=0.5}... ¡Puedo aceptarlos de vuelta cuando quieras!"

                "Mejor no.":
                    pass
                    
            jump beginbusiness

        ">Invertir dinero" if (not investment >= 100000 and HasEvent("Gardenia", "InvestmentIntro")):
            $ cost, purchaseprice, itemid, description = GetNextInvestmentPrize()
            $ name = GetItemName(itemid)
            $ moretoinvest = cost - investment
            $ formatdescription = description[0].lower() + description[1:]
            gardenia @happy "¡Ese es el tipo de actitud con mentalidad de tiburón que me gusta escuchar, mi queridísimo amigo!"
            gardenia @talkingmouth "Una vez que hayas invertido $[moretoinvest], llegando a un total de $[cost], debería poder conseguir un par de [name]. Luego te los ofreceré por $[purchaseprice]."
            gardenia @talking2mouth "Me parece que ese objeto [formatdescription]. ¡Aunque, mejor cómpralo y confirma si estoy en lo cierto!"
            gardenia @talkingmouth "Así que, ¿cuánto te gustaría invertir?"
            $ investing = renpy.input("¿Cuánto te gustaría invertir?", default=money, length=6, allow="1234567890")
            if (not investing.isdigit()):
                $ investing = 0
            else:
                $ investing = int(investing)

            if (investing > money):
                if (investing > bank):
                    gardenia @sadbrow talking2mouth "Lo siento. No creo que tengas el dinero para ese tipo de inversión y tampoco acepto criptomonedas."
                else:
                    gardenia @talkingmouth "No tienes dinero a la mano para eso, pero puedo sacarlo de tu cuenta, ¿te parece bien?"

                    menu:
                        "Seguro.":
                            $ bank -= investing
                            $ investment += investing

                            gardenia @happy "Tal vez tu cartera no sea de un gran inversor, pero tu espíritu seguro lo es. ¡Te lo agradezco, [first_name]!"

                        "Mejor no.":
                            pass

            elif (investing == 0):
                pass

            else:
                $ money -= investing
                $ investment += investing

                gardenia @happy "Tal vez tu cartera no sea de un gran inversor, pero tu espíritu seguro lo es. ¡Te lo agradezco, [first_name]!"

            if (investment >= 100000):
                gardenia @surprised "¡V-vaya! Estos números... ¡Parece que el mercado cambió en el momento perfecto!"
                gardenia @happy "[first_name], ¡has llevado mi línea de inversión al máximo! Y dejaste a {i}varios{/i} transportistas dudosos de Inspira muy contentos."

                red @sadbrow talkingmouth "¿G-genial?"

                if (investment > 100000):
                    gardenia  @talking2mouth "Te regreso una parte. Prefiero números cerrados, así que fijaré tu inversión conmigo en unos justos 100 mil."

                    $ money += (investment - 100000)

                    narrator "Gardenia te devolvió algo de dinero."

                gardenia @happy "Así es, ahora te estoy vendiendo {i}cada{/i} producto que puedo conseguir."
                gardenia @talkingmouth "Ah... Parece que tendré que inventar algo nuevo, algo {i}realmente{/i} grande, para que puedas invertir."

                red @sadbrow talkingmouth "Tal vez podremos hablar de eso el próximo año."

                gardenia @angrybrow talking2mouth "Yo {i}sin duda{/i} lo haré. Prepara esa cartera para mí, [first_name]."

                red @happy "¡Cuenta con ello!"

            jump beginbusiness

        ">Comprar" if (investment >= 1000):
            call screen shopkeep(marketitems, market=True)
            $ boughtitem = _return
            if (boughtitem == "Back"):
                gardenia @sadbrow talkingmouth "¿Por qué odias la economía y el libre mercado, [first_name]?"
                jump beginbusiness
            else:
                $ totalcost = boughtitem[0] * boughtitems
                if (totalcost > money):
                    narrator "¡No puedes permitirte comprar esto!"
                else:
                    $ itemname = GetItemName(boughtitem[1])
                    $ money -= totalcost 
                    if (boughtitems > 1):
                        narrator "¡Compraste [boughtitems] [itemname]s por un total de $[totalcost]!"
                    else:
                        narrator "¡Compraste un/a [itemname] por un total de $[totalcost]!"
                    $ GetItem(itemname, boughtitems)
                    $ boughtitems = 1

                jump beginbusiness

        ">Vender" if (persondex["Gardenia"]["Contact"]):
            gardenia @happy "Claro, te compraré algo. ¿Qué estás vendiendo?"

            label selling:

            python:
                global invoverwrite
                global itemdesc
                invoverwrite = None
                itemdesc = " "
                item = renpy.call_screen("fieldinventory", True)
            if (item == "back"):
                gardenia @angrybrow happymouth "¡Vaya, qué decepción!"
                jump beginbusiness
            else:
                $ itemvalue = GetItemSellValue(item)
                $ itemvalueformat = "{:,}".format(itemvalue)
                gardenia @talkingmouth "Mmm... no hay mucha demanda para este item. Lo mejor que puedo ofrecer es $[itemvalueformat]."

                $ itemcount = GetItemCount(item)
                $ halfitem = math.floor(itemcount / 2.0)

                menu:
                    ">Vender uno":
                        if (LoseItem(item)):
                            $ money += itemvalue
                            gardenia @happy "¡Encantada de hacer negocios!"

                    ">Vender la mitad ([halfitem])" if (itemcount >= 3):
                        if (LoseItem(item, halfitem)):
                            $ money += itemvalue * halfitem 
                            gardenia @happy "¡Encantada de hacer negocios!"

                    ">Vender todo ([itemcount])" if (itemcount > 1):
                        if (LoseItem(item, itemcount)):
                            $ money += itemvalue * itemcount
                            gardenia @happy "¡Encantada de hacer negocios!"

                    "Mejor no.":
                        pass

                jump selling

        "Mejor no.":
            gardenia @angrybrow happymouth "¡Vaya, qué decepción!"

    hide baseball
    hide gardenia 
    with dis
    jump aftersetup

elif (interaction == "Bees"):
    call combeefrenzy from _call_combeefrenzy

    if (not HasEvent("Whitney", "FrenzBee")):
        jump aftersetup

elif (interaction == "LevelCheck"):
    show stadium_empty
    show janine 
    with dis
    $ levelaim = AimLevel()
    $ highestlevel = GetHighestLevel()
    janine @surprised "¿Mmm?"
    janine @closedbrow talking2mouth "Oh, ¿quieres que te haga un chequeo? Deberías tener un equipo de Pokémon de nivel [levelaim]."
    janine @talking2mouth "Tu Pokémon de mayor nivel esta al nivel [highestlevel]. {nw}"
    if (highestlevel >= levelaim):
        extend @happymouth "Estas bien."
        if (highestlevel > levelaim + 5):
            janine @surprised "Quizás demasiado bien; ¿has pasado mucho tiempo entrenando, eh? No descuides tus otras responsabilidades."
    elif (highestlevel < levelaim):
        extend @sadbrow talkingmouth "Deberas entrenar más."
        if (highestlevel < levelaim - 5):
            janine @sad "En poco tiempo no será seguro estar en esta situación."

    red @talkingmouth "Gracias por el consejo."

    jump aftersetup

elif (interaction == "CriticalCheck"):
    show clouds
    show garden:
        zoom 0.625
    show kris
    with dis
    $ critrate = GetAverageProficiency() / 2.0
    kris @happy "Hola, [first_name]."
    kris @talkingmouth "¿Has estado al día con tus capturas? [bluecolor]Dadas tus habilidades actuales, puedes esperar obtener capturas críticas aproximadamente el [critrate]%% de las veces."

    red @talkingmouth "Entendido, gracias, Doctora."

    jump aftersetup

elif (interaction == "AccessPC"):
    $ currentbox = max(0, currentbox)
    show screen partymons
    call screen pokemonswap
    hide screen partymons
    jump aftersetup

elif (interaction == "CookingClub"):
    show mallow with dis

    mallow @happy blush "¡[first_name]! ¡Alola! Me alegra verte otra vez. ¿Vienes a unirte al Club de Cocina? ¿O solo quieres comprar unos Pokécubos?"

    red @talkingmouth "Por el momento, solo los Pokécubos."

    mallow @happy "¡Muy bien!"

    call screen shopkeep(treatitems)
    $ boughtitem = _return
    if (boughtitem == "Back"):
        mallow surprised "¡O-oh! ¡Entendido! Entonces, ¿nos vemos después?"

        jump aftersetup
    else:
        $ totalcost = boughtitem[0] * boughtitems
        if (totalcost > money):
            narrator "¡No puedes permitirte comprar esto!"
        else:
            $ itemname = GetItemName(boughtitem[1])
            $ cookingcredit += totalcost
            $ money -= totalcost 
            if (boughtitems > 1):
                narrator "¡Compraste [boughtitems]x [itemname] por un total de $[totalcost]!"
            else:
                narrator "¡Compraste un [itemname] por un total de $[totalcost]!"
            $ GetItem(itemname, boughtitems)
            $ boughtitems = 1

    jump aftersetup

elif (interaction == "Back"):
    jump aftersetup

elif (len(GetScenes([interaction])) == 1 and GetScenes([interaction])[0][1]):#character scenes
    $ renpy.hide(interactionsprite)
    $ renpy.show(interactionsprite, [farleftside, dissolvein])
    narrator "¿Quieres pasar el rato con [interaction]?"

    menu:
        "Sí, quiero pasar el rato con [interaction].":
            $ HangOutsThisWeek[interaction] = copy.copy(calDate)
            stop music fadeout 2.0
            $ renpy.hide(interactionsprite)
            $ renpy.call(GetScenes([interaction])[0][1])

            if (GetRelationshipRank(interaction) == 1 and not (interaction.title() == "Misty" and HasEvent("Misty", "Scene2Part1"))):
                if (interaction in classdex.keys()):
                    python:
                        classessstring = ""
                        classes = GetCharTypes(interaction)
                        for i, classname in enumerate(classes):
                            classessstring += (" and " if i == len(classes) - 1 else " ") + classname + ("," if i < len(classes) - 1 and len(classes) != 2 else "")

                    narrator "Al pasar tiempo con [interaction], se asignará una cantidad de EXP a los Pokémon de tipo [classessstring] en tu grupo. Esta cantidad crecerá conforme acumules más puntos con [interaction]."

                elif (interaction == "Janine"):
                    narrator "¡Tus Pokémon decidieron empezar a trabajar más duro para protegerte de la mujer aterradora."
                    narrator "(Ellos no entienden cómo es la dinámica en esta relación...)"

                    python:
                        for mon in playerparty:
                            mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 / 2))

            jump afterfreetime

        "Mejor no.":
            python:
                renpy.hide(interactionsprite)
                renpy.jump("freeroam")

else:
    if (interaction in ["Sabrina", "Blue", "Janine", "Misty", "Dawn", "Hilbert", "Professor Cherry"] and GetRelationshipRank(interaction) == 0):
        narrator "Sospechas que quizas no seas tan cercano a [interaction] para pasar el rato a solas..."
        jump aftersetup
    elif (interaction == "Janine"):
        if (HasEvent("Janine", "Domming")):
            narrator "Sabes que no debes molestar a Janine mientras está ocupada. Las posibles consecuencias te asustan y en parte te emocionan...{w=0.5} pero hay que dejarlas para otro momento."
        else:
            narrator "Sabes que no debes molestar a Janine mientras está ocupada."
        jump aftersetup
    elif (interaction == "Yellow"):
        narrator "Yellow está trabajando arduamente en la enfermería... No deberías molestarla ahora mismo."
        jump aftersetup
    else:
        $ renpy.hide(interactionsprite)
        $ renpy.show(interactionsprite, [farleftside, dissolvein])
        narrator "¿Quieres pasar el rato con [interaction]?"

        menu:
            ">Sí, quiero pasar el rato con [interaction].":
                python:
                    HangOutsThisWeek[interaction] = copy.copy(calDate)
                    renpy.transition(dis)
                    renpy.show(GetCharacterSprite(interaction, 10))
                    valuetochange = 3
                    if (interaction in ["Jasmine", "Grusha"]):
                        valuetochange = 6
                    ValueChange(interaction, valuetochange, 0.12)

                narrator "Pasas tiempo a solas con [interaction]."
                python:
                    if (GetRelationshipRank(interaction) >= 1):
                        partyset = set()
                        if (interaction in classdex.keys()):
                            for mon in playerparty:
                                for typename in GetCharTypes(interaction):
                                    if mon.HasType(typename):
                                        partyset.add(mon)
                        for mon in partyset:
                            mon.GainExperience(math.floor(pow(AimLevel(), 3) / 25 * (GetCharacterLevel(interaction) / 5)))

                    renpy.hide(interactionsprite)
                jump afterfreetime

            ">Dar un regalo" if (interaction not in GiftsGiven and persondex["Gardenia"]["Contact"]):
                python:
                    global invoverwrite
                    global itemdesc
                    invoverwrite = None
                    itemdesc = " "
                    item = renpy.call_screen("fieldinventory", True)
                if (item == "back"):
                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")
                else:
                    $ itemname = GetItemName(item)
                    menu:
                        ">Regalar a [interaction] el/la [itemname]":
                            if (LoseItem(item)):
                                python:
                                    presentvalue = GetGiftValue(interaction, item)
                                    renpy.show(GetCharacterSprite(interaction, presentvalue))
                                    if (presentvalue < 1):
                                        renpy.say(None, "Juras haber visto a {} llorar mientras tomaba el/la {}...".format(interaction, itemname))
                                    elif (presentvalue == 1):
                                        renpy.say(None, "{} parece confudido/a, pero acepta cortésmente el/la {}.".format(interaction, itemname))
                                    elif (presentvalue == 2):
                                        renpy.say(None, "{} acepta el/la {}.".format(interaction, itemname))
                                    elif (presentvalue == 3):
                                        renpy.say(None, "{} acepta felizmente el/la {}.".format(interaction, itemname))
                                    elif (presentvalue == 4):
                                        renpy.say(None, "{} acepta alegremente el/la {}.".format(interaction, itemname))
                                    elif (presentvalue >= 5):
                                        renpy.say(None, "{} acepta con euforía el/la{}!".format(interaction, itemname))
                                    if (interaction in ["Jasmine", "Grusha"]):
                                        presentvalue *= 2
                                    GiftsGiven.append(interaction)
                                    if (presentvalue > 10):
                                        ValueChange(interaction, 10, 0.12, pausing=False, changemood=False)
                                        ValueChange(interaction, presentvalue - 10, 0.24, changemood=False)
                                    else:
                                        ValueChange(interaction, presentvalue, 0.12, changemood=False)

                        "Mejor no.":
                            pass

                    $ renpy.hide(interactionsprite)
                    $ renpy.jump("freeroam")

            "Mejor no.":
                python:
                    renpy.hide(interactionsprite)
                    renpy.jump("freeroam")

label afterfreetime:
$ freeroaming = False
call clearscreens from _call_clearscreens_18

python:
    if (IsAfter(30, 4, 2004)):
        added = UpdateForeverals()
        if (len(added) > 0 and pikachuobj in playerparty):
            renpy.say(None, "¿Eh? [pika_name] empezo a toser... ¡Algo salió de su boca!")
            for key, value in added.items():
                count = len(value)
                if count == 1:
                    reward = value[0]
                    renpy.say(None, f"¡Tu vínculo con {key} te ha otorgado un/a {reward}!")
                else:
                    rewards = ', '.join(value[:-1])
                    last_reward = value[-1]
                    exclamation_marks = '!' * math.ceil(count / 3)
                    renpy.say(None, f"¡Tu vínculo con {key} te ha otorgado un/a {rewards}, y {last_reward}{exclamation_marks}")
            
            if (IsAfter(8, 5, 2004) and persondex["Yellow"]["Value"] != 0):
                persondex["Yellow"]["Value"] = len(claimedforeverals)
                renpy.say(None, "¡Yellow esta rebosando de felicidad!")

hide blank2
show blank2

pause 1.0

if (timeOfDay == "Morning"):
    $ timeOfDay = "Noon"
elif (timeOfDay == "Noon" or timeOfDay == "Afternoon"):
    $ timeOfDay = "Evening"
elif (timeOfDay == "Evening" or timeOfDay == "After School"):
    if (excusesecondhomeroom):
        $ jumpto = "aftersecondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)
    else:
        $ timeOfDay = "Night"

hide noon
hide evening
hide night

if (timeOfDay == "Noon"):
    show noon at vspaz
elif (timeOfDay == "Evening"):
    show evening at vspaz
    if (not excusesecondhomeroom and getRWDay(0) not in ["Saturday", "Sunday"]):
        pause 3.0

        $ jumpto = "secondhomeroom"
        $ jumptoyear = "01"
        $ jumptomonth = ("0" if calDate.month < 10 else "") + str(calDate.month)
        $ jumptodate = ("0" if calDate.day < 10 else "") + str(calDate.day)
        $ renpy.jump(jumpto + jumptoyear + jumptomonth + jumptodate)

elif (timeOfDay == "Night"):
    show night at vspaz

    pause 3.0

    show screen currentdate with dis

    call nightscenequeue from _call_nightscenequeue

    return

pause 3.0

if (IsDate(29, 5, 2004)):
    if (timeOfDay == "Noon"):
        jump nooncontestintermission

    else:
        jump eveningcontestintermission

jump beforemusic

label cyclizarhunt:
    $ AddEvent("Dawn", "CyclizarHunt")
    $ renpy.music.queue("audio/music/Fieldstheme_Start.ogg", channel='music', loop=None, fadein=1.0, tight=None)
    $ renpy.music.queue("audio/music/Fieldstheme_Loop.ogg", channel='music', loop=True)
    show clouds:
        yalign 0.5
    show fields1 :
        yalign 0.33 xalign 0.95
    with Dissolve(2.0)
    show blank2 as blackground behind map

    show leaf with dis:
        xpos 0.66

    show dawn with dis:
        xpos 0.33

    dawn @talkingmouth "{size=-15}... Así que pensé{/size} {size=-10}en que quizás podría intentar{/size} {size=-5}ayudarla{/size}."

    leaf @talkingmouth "¡Suena como una gran idea! Apuesto que una entrenadora tan ansombrosa como tu puede capturar {i}gran{/i} cantidad de Cyclizar."
    leaf @angrybrow talking2mouth "¡Ooh, tal vez podamos lograr que ella no tenga que pagar ni un solo Pokécentavo de su propio bolsillo!"

    dawn @sadbrow talkingmouth "E-eso sería... genial... pero, uhm, no creo que todos puedan montar un Cyclizar no entrenado sin tener {i}mucha{/i} práctica..."

    leaf @talking2mouth "¡Bueno, haremos nuestro mejor esfuerzo! Es mejor tener las herramientas y no necesitarlas que dejarle todo a la Profesora Cherry."
    leaf @sadbrow talking2mouth "Después de todo... si lo que dijo sobre cómo hemos progresado hasta ahora es cierto... entonces {i}definitivamente{/i} merece nuestro agradecimiento. Es lo mínimo que podemos hacer para mostrar nuestra gratitud."

    dawn @talkingmouth "S-sí, tienes razón."

    pause 1.0

    if (not HasEvent("Ethan", "IgnoredFrenzyConfession")):
        dawn @surprised "¡O-oh! ¡Eres tú, rival!"

        red @talkingmouth "Ese es mi nombre."

        leaf @talking2mouth "¿Ustedes dos ahora son rivales?"

        dawn @talkingmouth "S-sí, lo uhm... decidimos el pasado miércoles."

        red @talkingmouth sweat "Más bien lo decidiste tú."

        dawn @sadbrow "Oh... lo siento..."

        red @happy "No, no lo entiendes. ¡Eso es {i}genial{/i}! Me {i}alegra{/i} hayas tomado esa decisión."

        red @talkingmouth "Siempre te apoyare en lo que te apasione."

        if (GetRelationship("Dawn") == "Muse"):
            red @happy "Por eso soy tu musa, ¿no?"

            $ ValueChange("Dawn", 2, 0.33, False)

        else:
            $ ValueChange("Dawn", 1, 0.33, False)
    
        leaf @happy "Aww. Honestamente, ustedes dos son demasiado adorables."

        $ ValueChange("Leaf", 1, 0.66)
    
    else:
        leaf @happy "¡Oh, hola! No te había visto ahí."

    red @talkingmouth "Pensé que podría venir a ver si puedo atrapar unos Cyclizars para la Profesora. ¿Les importa si me les uno?"

    dawn @talkingmouth "¡Claro que no! Eh... eso suena genial. ¡Entre más, mejor!"

    red @talkingmouth "Perfecto. ¡Manos a la obra!"

    leaf @surprised "...{w=0.5} Ah, espera. Hay un pequeño detalle... No sé si traigo suficientes Poké Balls conmigo."

    show gardenia angrybrow happymouth:
        xpos 1.2 
        ease 0.3 xpos 0.75

    show dawn surprisedbrow frownmouth:
        xpos 0.33
        ease 0.5 xpos 0.25

    show leaf surprisedbrow frownmouth:
        xpos 0.66
        ease 0.5 xpos 0.5 xzoom -1

    gardenia "¡Y {i}ahí{/i} es donde entro yo!"

    pause 1.0

    dawn "{size=30}Oh no, ¿ella otra vez?{/size}"

    gardenia -angrybrow -happymouth @happybrow talking2mouth "Guarden sus aplausos, por favor."

    red @talking2mouth confusedeyebrows "Perdón, ¿qué está pasando aquí exactamente?"

    gardenia @talkingmouth "Oí que necesitan Poké Balls."
    gardenia @happybrow talkingmouth "Además, tengo Repelentes para que encuentren a esos Cyclizar más rápido ¡Y con precios que no podrán rechazar!"

    leaf @sarcastic "¿Nos estabas, digamos, siguiendo y esperando a que alguien necesitara algo?"

    gardenia @talkingmouth "¡Qué gracioso! Pero no me puedo quedar mucho tiempo, otros clientes me esperan."
    gardenia @talkingmouth "Así que, ¿alguno esta interesado en mi oferta?"

    $ discountask = False
    $ priceone = 4000
    $ pricetwo = 10000
    $ pricethree = 15000

    label gardeniafieldshustle:

    menu:
        "10 Poké Balls & 3 Repelentes por $[priceone]":
            if (money >= priceone):
                $ money -= priceone
                $ GetItem("Poké Ball", 10)
                $ GetItem("Repel", 3)
                $ ValueChange("Gardenia", 1, 0.75)

                gardenia @happy "¡Encantada de hacer negocios!~ ¿Necesitan algo más?"

            else:
                gardenia @sadbrow talking2mouth "Lo siento, [first_name]. No puedo darte crédito. Vuelve cuando seas un poco más... mmm... ¡Rico!"

            jump gardeniafieldshustle

        "10 Great Balls & 3 Super Repelentes por $[pricetwo]":
            if (money >= pricetwo):
                $ money -= pricetwo
                $ GetItem("Great Ball", 10)
                $ GetItem("Super Repel", 3)
                $ ValueChange("Gardenia", 2, 0.75)

                gardenia @happy "¡Encantada de hacer negocios!~ ¿Necesitan algo más??"

            else:
                gardenia @sadbrow talking2mouth "Lo siento, [first_name]. No puedo darte crédito. Vuelve cuando seas un poco más... mmm... ¡Rico!"

            jump gardeniafieldshustle

        "10 Ultra Balls & 3 Repelentes Máximos por $[pricethree]":
            if (money >= pricethree):
                $ money -= pricethree
                $ GetItem("Ultra Ball", 10)
                $ GetItem("Max Repel", 3)
                $ ValueChange("Gardenia", 3, 0.75)

                gardenia @happy "¡Encantada de hacer negocios!~ ¿Necesitan algo más?"

            else:
                gardenia @sadbrow talking2mouth "Lo siento, [first_name]. No puedo darte crédito. Vuelve cuando seas un poco más... mmm... ¡Rico!"

            jump gardeniafieldshustle

        "¿Qué hacen los repelentes?":
            gardenia @happy "¡Buena pregunta!"
            gardenia @talkingmouth "Los Repelentes tienen dos funciones:"
            gardenia @talkingmouth "Por un lado, {i}todos{/i} los Repelentes te permiten escapar automáticamente de un combate."
            gardenia @happy "Y, por el otro, no necesitas usarlos {i}durante{/i} una batalla; también funcionan fuera del combate y duran aproximadamente... veinte encuentros."

            gardenia @talkingmouth "De todos modos, cada tipo de Repelente mantiene alejados a ciertos Pokémon."
            gardenia @talkingmouth "Los normales alejan a los Pokémon más débiles, así que solo aparecerán los más fuertes, lo que significa que los Pokémon comunes de la zona no se presentarán."
            gardenia @happy "Los Súper Repelentes suben la apuesta: eliminan a casi todos los Pokémon más débiles, dejando únicamente a los verdaderamente fuertes."
            gardenia @talkingmouth "Finalmente... si es que quieres el {i}verdadero{/i} poder..."
            gardenia @happy "Los Máximos Repelentes los cuales permiten que solo aparezcan los Pokémon más fuertes de todos: los líderes de las manadas, los veteranos del enjambre, los pesos pesados..."
            gardenia @talkingmouth "Eso significa que solo verás a los Pokémon más poderosos del lugar, esos que normalmente te llevaría horas o incluso {i}días{/i} en encontrar. ¡Son Repelentes muy potentes!"
            gardenia @angrybrow happymouth "Y mi {i}recomendación personal{/i}, si buscas llevar tus encuentros al siguiente nivel."

            jump gardeniafieldshustle

        "¿Puedes darme un descuento?" if (not discountask):
            $ discountask = True
            show gardenia surprisedbrow frownmouth with dis

            pause 0.5

            gardenia @talkingmouth "Hmm, eso si que es tener agallas."

            if (investment == 0):
                gardenia @talkingmouth "Lo siento, amigo, mis descuentos son solo para socios establecidos."
                gardenia @talkingmouth "Si te interesa serlo, pásate por el campo de béisbol alguna vez y hablaremos de negocios."

            elif (investment < 10000):
                $ priceone = 3500
                $ pricetwo = 9500
                $ pricethree = 14500
                gardenia -surprisedbrow -frownmouth @happy "¿Sabes qué? ¡Qué demonios! Te hare un descuento de $500, como gesto de buena fe por nuestra asosiación."

            else:
                $ priceone = 3000
                $ pricetwo = 9000
                $ pricethree = 14000
                gardenia -surprisedbrow -frownmouth @happy "¿Sabes qué? ¡Qué demonios! Te hare un gran descuento de $1000, como gesto de buena fe por nuestra asosiación."

            jump gardeniafieldshustle

        "¡Fuera de aquí, emisario del capitalismo!":
            gardenia @happy "Como prefieras."

    gardenia @angrybrow talkingmouth "Bien, ¿y {i}ustedes{/i}, encantadoras damas...?"

    show blank2 with dis

    narrator "Gardenia prácticamente obliga a Dawn a adquirir una cantidad absurda de productos hasta que Leaf la ahuyenta de forma bastante directa."

    show leaf -surprisedbrow -frownmouth:
        xpos 0.66 xzoom 1
    show dawn:
        xpos 0.33
    hide blank2 
    hide gardenia
    with dis

    dawn -surprisedbrow frownmouth @sadbrow talkingmouth "Yo... no sé cómo decir que no cuando intentan venderme algo..."

    leaf @talkingmouth "Eso es obvio. Más vale mantenerte lejos de {i}Join.{/i} El vendedor de crema nasal ahí te comería viva."

    return

label combeefrenzy:
    scene baseball
    show whitney
    with splitfade

    if (activetreat in [Item.PicnicBasket, Item.BouffalantWings]):
        $ AddEvent("Whitney", "FrenzBee")
        whitney @talking2mouth "¡Oh, [first_name]! ¡Llegaste en el momento perfecto!"

        red @confusedeyebrows talkingmouth "¿Qué? ¿Dices que la abeja amante del jazz que te coqueteó está aquí?"

        whitney surprised "¡Eh, sí!"

        red @surprised "¿Qué?"

        $ renpy.music.queue("Audio/Music/RelicCastle_Start.ogg", channel='music', loop=False, tight=None, fadein=3.0)
        $ renpy.music.queue("Audio/Music/RelicCastle_Loop.ogg", channel='music', loop=True, tight=None)

        whitney @sad "¡Ah! ¡Está regresando! ¡Y soy alérgica a las picaduras de abeja!"

        show whitney:
            xpos 0.5
            ease 0.3 xpos -0.5

        red @surprised "Wait, really?"

        $ sidemonnum = 415

        $ PlaySound("pokemon/cries/415.mp3")

        sidemon "¡Linda! ¡Linda! ¡Linda!"

        show sideportraitfull:
            xpos 1.1 zoom 0.0 ypos 0.0 yanchor 1.0 xanchor 0.5
            ease 1.0 xpos 0.5 zoom 2.0 ypos 1.0
            ease 1.0 xpos 0.2 zoom 0.5 ypos 0.3
            easeout 1.0 xpos 0.5 zoom 1.0 ypos 0.4
            easein 1.0 zoom 3.0 ypos 1.2

        red @surprised "¿En serio {i}es{/i} un Combee? Pero... ¿no te parece algo extraño...?"

        show sideportraitfull:
            ease 0.3 zoom 2.0 align (0.5, 0.5) alpha 1.0

        sidemon "¡Linda! ¡Linda! ¡Linda!"

        python:
            trainer1 = Trainer("red", TrainerType.Player, playerparty, number=3)

            vespiquenobj = Pokemon("Vespiquen", level=33.3, moves=[GetMove("Attack Order"), GetMove("Defend Order"), GetMove("Heal Order"), GetMove("Acrobatics")], gender=Genders.Female, item="Sitrus Berry", foreverals=["Vespiquen Uneveral"], frenzynerf=(21, ["Slash", "Bug Bite", "Defend Order", "Power Gem"]), intelligence=3)
            vespiquenobj.ApplyStatus("frenzied")
            vespiquenobj.Image = "pokemon/415.webp"
            vespiquenobj.Nickname = "Combee"
            trainer2 = Trainer("sideportraitfull", TrainerType.Enemy, [vespiquenobj], isPokemon=True)

        call Battle([trainer1, trainer2], healParty = False, specialmusic="Nothing", custombrain=combeebrain) from _call_Battle_168
        $ battlehistory["Combee1"]  = _return

        stop music fadeout 1.5

        pause 2.0

        queue music "audio/music/goldenrod_start.ogg" noloop
        queue music "audio/music/goldenrod_loop.ogg"

        show whitney:
            xpos -0.2
            ease 2.0 xpos 0.0 rotate 25

        pause 0.5

        whitney sadbrow @talking2mouth "¿Ya se fue?"

        red @talkingmouth sweat "Sí, ya se fue."

        $ ValueChange("Whitney", 3, 0.05)

        show whitney:
            xpos 0 rotate 25
            ease 0.5 xpos 0.5 rotate 0

        whitney -sadbrow @talking2mouth "¡Uf, gracias por la ayuda!"
        whitney @surprised "Pero, espera, ¿cómo es que estaba hablando japonés?"

        red @talkingmouth "No creo que estuviera hablando japonés en absoluto."
        red @closedbrow talking2mouth "Cuando lo enfrenté, pude ver que tenía un Foreveral."
        red @sideeyes talking2mouth "Es raro, pero ya he visto algo parecido antes." 
        red @talking2mouth "Sin embargo, este parecía que se estaba ahogando con él."
        red @sadbrow talkingmouth "Ese sonido de asfixia seguro fue lo que escuchaste, parecía decir '¡Hog! ¡Hog! ¡Hog!'"

        whitney sadbrow frownmouth @sad "¡Oh no! ¡Pobre cosita! ¿Deberíamos llevarlo para que lo atiendan?"

        if (vespiquenobj in AllPokemon()):
            red @talking2mouth "No lo creo, capturarlo destruyó el Foreveral."

        elif (WonBattle("Combee1")):
            red @closedbrow talking2mouth "No lo creo, parecía estar bien después de que lo derroté. Pienso que con suficientes combates el Foreveral terminó rompiéndose."

        else:
            red @sweat sadbrow talkingmouth "Digo, viste cómo me dio una paliza, ¿no? Estoy bastante seguro de que está bien. Pude ver que sacó el Foreveral antes de volar, aunque se hizo pedazos antes de caer al suelo."

        whitney -sadbrow -frownmouth @talkingmouth "...Bueno, eso está bien, pero queda una última pregunta en el aire..."

        red @confused "¿Sí?"

        whitney @confusedbrow talkingmouth "¿Cómo es que me preguntó si me gusta el jazz?"

        red @closedbrow talking2mouth "Caray, olvidé esa parte. La verdad, no tengo idea. ¿Quizá había una radio cerca?"

        whitney @confusedeyebrows talking2mouth "[first_name], es 2004. Ya no quedan radios {i}en uso.{/i}"

        red @closedbrow talkingmouth "Vale, vale. Puedes presumir tu superioridad tecnológica después. Ahora debo irme."

        whitney @happy "¡Gracias por despejar el campo de béisbol!"

        red @talkingmouth "De nada."

        scene blank2 with splitfade

        pause 2.0

        call clearscreens() from _call_clearscreens_234
        scene baseball
        show flannery at leftside:
            xpos 0.33 xzoom -1
        with splitfade

        Character("???") "\"¿Te gusta el jazz?\""

        show flannery:
            xpos 0.33
            ease 0.5 xzoom 1

        flannery @talking2mouth "¿Eh? ¿Jazz? Bueno, supongo que está bien. ¿Te conozco?"

        show brock:
            xpos 1.2 xzoom -1
            ease 0.5 xpos 0.66

        brock @talkingmouth "Probablemente no. Soy como una vela al viento, nena."
        brock @happymouth "Ardiendo un momento... y consumido al siguiente."

        flannery @confusedbrow talking2mouth "Uhm... ¿Deberías estar aquí?"

        brock @talkingmouth "¿Acaso alguien está realmente donde debería estar?"

        pause 1.0

        brock surprised @happy "Jeje~. Noté que tienes un Onix, es una opción bastante sólida. Yo también tengo uno..."

        pause 1.0

        flannery tired @tiredbrow talking2mouth "Te juro por Dios y todos los santos que si te llegas a bajar los pantalones, haré que mi Numel queme lo que sea que tengas debajo."

        brock sadbrow @sad "¡Wo-hoh! Te equivocas, pequeña. Solo... eh, solo estaba preguntando cosas como..."

        pause 1.0

        brock sadbrow happymouth "¿Te gusta la cumbia?"

        scene blank2 with splitfade

    else:
        red @talkingmouth "Hey Whitney, ¿haz visto a ese Combee del que hablas?"

        whitney @talking2mouth "Por el momento no, pero sigue viniendo al campo... ¡y {i}juro{/i} que me llama linda!"

        red @closedbrow talkingmouth "Eso habrá que verlo."

        whitney @upeyes talking2mouth "Si queremos que vuelva... hmm, parece aparecer más cuando Flanny y yo hacemos picnic aquí..."
        whitney @sadbrow talking2mouth "¿Quizá eso ayude?"

        red @closedbrow talking2mouth "Puede ser. Aunque, creo que ya tengo una idea."

        if (GetItemCount(Item.PicnicBasket) > 0 or GetItemCount(Item.BouffalantWings)):
            redmind @thinking "Si viniera aquí oliendo a un Pokécubo que le guste a Combee, entonces quizás..."

    return
