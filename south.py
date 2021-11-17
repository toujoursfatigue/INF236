import pandas as pd
import base64
import re
import streamlit as st

#jaccard similarity
def jaccard_similarity(list1, list2):
    intersection = len(set(list1).intersection(list2))
    union = len(set(list1)) + len(set(list2)) - intersection

    return intersection / union

def random_jaccard_recommandation(user_input):
    jaccard_similarity_list = []
    user_input = user_input.lower()

    if user_input in categories_name:
        n = categories_name.index(user_input)
        recommendation = df["sentence"][df["category"] == user_input].sample().values[0]

        return recommendation
    else:
        if len(user_input.split()) > 1:
            for i in range(len(df)):
                jaccard_similarity_list.append(jaccard_similarity(df["sentence_c"][i], user_input))
                max_index = jaccard_similarity_list.index(max(jaccard_similarity_list))
                recommendation = df['sentence'][max_index]
        else:
            recommendation = df["sentence"].sample().values[0]
        return recommendation

#south park bölümleri listesi
south_park = """
"Cartman Gets an Anal Probe"
While the boys are waiting for the school bus, Cartman explains the odd nightmare he had the previous night involving alien visitors.

"Weight Gain 4000" 
When Cartman's environmental essay wins a national contest, America's sweetheart, Kathie Lee Gifford, comes to South Park to present the award.

"Volcano"
A weekend trip to experience the finer points of camping, fishing and blowing animals to smithereens is threatened by an erupting volcano.

"Big Gay Al's Big Gay Boat Ride"
When Stan discovers his new dog Sparky is gay, he becomes so confused he loses his will to play in the big Homecoming Football game against North Park.

"An Elephant Makes Love to a Pig"
Kyle's mom won't let him keep his new pet, an elephant because it's so huge. So the boys turn to Dr. Mephesto to genetically engineer a smaller elephant.

"Death"
Grandpa's sole birthday wish is for Stan to take part in his assisted suicide. Meanwhile, Mrs. Broflovski has organized a protest against the boys' favorite TV show, "Terrance and Phillip".

"Pinkeye"
A mishap at the morgue transforms the residents of South Park into brain-eating zombies and threatens the boys' night of Trick-or-Treating.

"Starvin' Marvin"
Mistaking Cartman for a starving African child, government authorities send him to Ethiopia where he runs into Sally Struthers.

"Mr. Hankey, the Christmas Poo"
While South Park Elementary is attempting to stage a non-denominational holiday play that won't offend (or entertain) anyone, Kyle checks himself into the South Park mental asylum.

"Damien"
After being shunned by the others kids, Damien, the Son of Satan, calls upon his father to fight Jesus in the ultimate Pay-Per-View Boxing Match between good and evil.

"Tom's Rhinoplasty"
While Mr. Garrison deserts the class for a visit to Tom's Rhinoplasty, Stan, Kyle, Kenny, and Cartman all compete for the attention of Ms. Ellen, the new substitute teacher.

"Mecha-Streisand"
The boys' discovery of a prehistoric relic spawns a monster that threatens to destroy South Park and the world.

"Cartman's Mom is a Dirty Slut"
Who is Eric Cartman's father? It could be anyone who attended South Park's 12th Annual Drunken Barn Dance.

"Terrance and Phillip in Not Without My Anus"
Terrance and Phillip must save Terrance's little daughter, Sally, and all of Canada from an evil dictator.

"Cartman's Mom is Still a Dirty Slut"  
The boys wait for Dr. Mephesto to regain consciousness and reveal the identity of Cartman's father.

"Ike's Wee Wee"    
Mr. Mackey, the school counselor, is fired and turns to drugs and alcohol. Meanwhile, when the boys find out what it means to be circumcised they try to save Ike from his bris.

"Chickenlover" 
When Barbrady resigns, anarchy ensues and the boys pitch in to help.

"Conjoined Fetus Lady"
The boys go to China to compete in a dodgeball championship. The town holds an appreciation week for the school nurse.

"The Mexican Staring Frog of Southern Sri Lanka"
Jimbo and Ned's efforts to drive up the ratings for their new hunting show on the cable access channel threatens to edge out an old favorite, Jesus and Pals.

"City on the Edge of Forever (Flashbacks)"
A freak accident leaves the South Park Elementary school bus teetering precariously on the edge of a cliff.

"Summer Sucks"
The entire town is gearing up for the annual 4th of July celebration when a ban on fireworks is imposed.

"Chef's Chocolate Salty Balls"
South Park's first film festival attracts crowds of pretentious, tofu-eating movie lovers to the quiet mountain town.

"Chickenpox"
The kids' parents only have their best interests at heart when they arrange for Stan, Kyle and Cartman to be exposed to the chickenpox virus.

"Roger Ebert Should Lay off the Fatty Foods"
Is the new planetarium a harmless place to learn about the solar system, or the scene of a diabolical plot to control the minds of South Park's citizens?

"Clubhouses"
Stan and Kyle are psyched to have Wendy and Bebe visit their clubhouse for a game of Truth or Dare, but first they have to build one.

"Cow Days" 
South Park's 14th Annual "Cow Days" rodeo and carnival is here and the boys are determined to win Terrance and Phillip dolls.

"Chef Aid" 
After a huge loss in court, Chef is left penniless, but he has some very famous and talented friends in the music business who want to help their old mentor.

"Spookyfish"   
When Sharon Marsh's Aunt Flo makes a monthly visit, she brings a mysterious pet fish for Stan.

"Merry Christmas Charlie Manson!"  
Dinner with Cartman's family takes a bizarre twist when Uncle Howard shows up after breaking out of prison with the help of his cellmate, Charlie Manson.

"Gnomes"   
Cartman, Stan, Kyle and Kenny are assigned to write a report with Tweek, the very nervous and highly caffeinated boy who insists gnomes are stealing his underpants.

"Prehistoric Ice Man"  
The boys' discovery of a man encased in ice threatens Stan and Kyle's friendship.

"Rainforest Shmainforest"  
The boys travel to the Costa Rica as a part of the "Getting Gay with Kids" choir tour.

"Spontaneous Combustion"
When the citizens of South Park start exploding randomly, the mayor enlists Stan's dad, the resident geologist, to find a solution to the problem.

"The Succubus" 
Chef's parents arrive in South Park from Scotland fresh from an encounter with the Loch Ness Monster to attend Chef's wedding.

"Jakovasaurs"  
The boys discover a prehistoric creature called a Jakovasaur while camping at Stark's Pond.

"Tweek vs. Craig"  
The boys instigate a fight between Tweek and Craig in shop class. Meanwhile, Mr. Adler, the shop teacher, is haunted by a recurring dream of his lost love.

"Sexual Harassment Panda"  
After Sexual Harassment Panda "educates" the children, Cartman sues Stan for sexual harassment, and a flurry of other lawsuits follow.

"Cat Orgy" 
While all the adults are gathering at Mr. Mackey's house to watch a meteor shower Shelly Marsh is left babysit Cartman.

"Two Guys Naked in a Hot Tub"
Stan's parents drag him along to Mr. Mackey's meteor shower party, where he is sent down into the basement to play with Pip, Butters and Dougie.

"Jewbilee" 
Kyle invites Kenny to join him and Ike at Jewbilee, a camp for Jewish kids.

"Korn's Groovy Pirate Ghost Mystery"
Korn comes to South Park for a Halloween concert and helps the boys solve a spooky pirate ghost mystery.

"Chinpokomon"  
Stan, Kyle, Cartman and Kenny are caught up in the latest fad from Japan: Chinpoko Mon!

"Hooked on Monkey Fonics"
To help Cartman win the school spelling bee, Cartman's Mom gives him the Hooked on Monkey Fonics spelling system.

"Starvin' Marvin in Space"
Starvin' Marvin returns to South Park with an alien spaceship and enlists Cartman, Stan, Kyle and Kenny's help to seek out a new home for his starving people.

"The Red Badge of Gayness" 
Cartman has visions of glory as he suits up for the Confederacy in the annual reenactment of a Civil War battle, and leads the drunken rebels to defeat the union.

"Mr. Hankey's Christmas Classics"  
An extravaganza of holiday songs are performed in unique South Park style, hosted by Mr. Hankey.

"Are You There God? It's Me, Jesus"    
People from all over the world start to gather outside Jesus' house waiting for a millennium miracle.

"World Wide Recorder Concert"
The children of South Park are invited to Arkansas for the "Four Million Child Blow 2000," the first worldwide recorder concert.

"The Tooth Fairy Tats 2000"
When Cartman discovers the Tooth Fairy is paying a premium price for his lost teeth, he and the boys seize the opportunity to make some cash.

"Cartman's Silly Hate Crime 2000"
Cartman is pursued by the FBI for committing a hate crime and lands in juvenile hall.

"Timmy 2000"
When Timmy is diagnosed with Attention Deficit Disorder, it triggers a wave of prescription drug abuse at South Park Elementary.

"Quintuplets 2000"
8-year-old contorting quintuplets from Romania defect to the United States and seek shelter with Stan's family.

"Cartman Joins NAMBLA"
Cartman decides to seek friendship using the Internet, and finds an older man who is more than willing to be his friend...and more.

"Cherokee Hair Tampons"
Kyle needs a kidney transplant and Cartman is discovered to be the perfect donor. Cartman gladly offers his kidney to Kyle -- for the price of $10 million dollars.

"Chef Goes Nanners"    
Chef's passionate protest declaring the South Park flag racist enflames the entire town.

"Something You Can Do with Your Finger"
"Fingerbang" is the newest boy band starring all the boys and it's also Cartman's latest scheme to make a million dollars.

"Do the Handicapped Go to Hell?"
The boys learn in Sunday school that they must confess their sins, but worry about Timmy since all he can say is his own name.

"Probably"
Cartman's flock begins to grow and the children begin plans to build him a Church. Meanwhile, Satan turns to God for advice.

"Fourth Grade"
The boys devise a plan to travel back in time a full year and return to the third grade, with the help of Timmy and his electronic wheelchair.

"Trapper Keeper"
When Cartman finally stops bragging about his new Trapper Keeper, a stranger informs him that it will eventually take over the world and destroy humankind, if they don't destroy it first.

"Helen Keller! The Musical"
When Butters informs the fourth graders that the Kindergarteners' school play is a magnificent sight to behold, they go through a lot of pain to make sure they beat the tiny tots' show.

"Pip"
When Pip is offered the opportunity to become a gentleman he goes to London only to discover that Miss Havisham plans to break his heart.

"Fat Camp"
Cartman's family and friends have intervened and are forcing him to trim down. While Cartman's away, Kenny's star is on the rise when he gets his own reality TV show.

"The Wacky Molestation Adventure"
To get back at his parents for not letting him go to a concert, Kyle tells the police that his parents molested him. Soon, the whole town is free of adults and divided into two rival cities.

"A Very Crappy Christmas"
When Mr. Hankey skips Christmas, the boys find him living with his alcoholic wife and their three little nuggets. He tells them that no one is into Christmas anymore.

"It Hits the Fan"  
The boys and Chef must stop the world from chanting the curse word "shit" because when spoken it causes people to "puke their own guts out".

"Cripple Fight"    
Big Gay Al becomes the boys' scoutmaster and a fight ensues between two handicapped children, Jimmy Swanson and Timmy.

"Super Best Friends"   
A cult comes to South Park and it is up to Stan, Jesus and his super hero comrades to save the world.

"Scott Tenorman Must Die"  
Cartman repeatedly tries to take revenge on an 8th/9th grader who keeps making fun of him.

"Terrance and Phillip: Behind the Blow"    
The boys try to reunite Terrance and Phillip who are feuding so they can perform at an Earth Day assembly.

"Cartmanland"  
Kyle develops a deadly hemorrhoid and begins to lose his faith in God when Cartman inherits $1 million from his grandmother, which he uses to buy his own amusement park.

"Proper Condom Use"    
The school is forced to teach sex education to the students at a younger age after the boys are found "milking" dogs.

"Towelie"
In order to get their video game console back, the boys must bring a talking towel to the government.

"Osama bin Laden Has Farty Pants"  
The boys go to Afghanistan to return a goat given as a gift.

"How to Eat with Your Butt"
Cartman puts Kenny's picture on a milk carton which brings a family from another state looking for him.

"The Entity"   
Kyle's cousin, who is also named Kyle, comes to stay in South Park.;Mr. Garrison, tired of the airlines, decides to invent his own vehicle.

"Here Comes the Neighborhood"  
Token is tired of being teased for being rich, and he brings wealthier families to South Park.

"Kenny Dies"
Kenny succumbs to an illness; Cartman acquires stem cells for research.

"Butters' Very Own Episode"
Butters goes on a chase to find out what his father bought his mother for their anniversary.

"Jared Has Aides"
After meeting Jared Fogle, famous for losing weight by eating Subway sandwiches, the boys form a get-rich-quick scheme involving Butters becoming the weight-loss spokesman for City Wok.

"Asspen"
The boys and their parents travel to Aspen for a winter vacation. Stan is challenged by teenagers to a ski race while the boys' parents are trapped at a TimeShare meeting.

"Freak Strike" 
The boys convince Butters to appear on "The Maury Povich Show" with a fake facial deformity in order to receive the show's prizes.

"Fun with Veal"    
The boys are on a mission to rescue a bunch of baby cows from certain slaughter.

"The New Terrance and Phillip Movie Trailer"   
The boys are anxious to see a new movie trailer during a commercial break, and, after Stan's TV is destroyed, frantically run around town in search of a working TV.

"Professor Chaos"  
Butters decides to wreak havoc on South Park as a super-villain after being relieved of his duty of being the boys' new fourth friend. Meanwhile, the boys hold auditions to find a replacement friend.

"The Simpsons Already Did It"  
Professor Chaos (Butters) proposes numerous evil plans, only to be informed by General Disarray (Dougie) that they have been done before. Cartman builds a miniature society with aquarium creatures.

"Red Hot Catholic Love"    
Priest Maxi attempts to uncover the Catholic Church's child molestation cases; South Park parents convert their families to atheism. Oh, and people crap out of their mouths.

"Free Hat"
Stan, Kyle, Cartman, and Tweek are on a mission to stop Steven Spielberg and George Lucas from editing their classic films, though the boys' supporters are more concerned about freeing a certain criminal from prison.

"Bebe's Boobs Destroy Society"
At exactly the same time Bebe starts developing breasts, the boys of South Park Elementary suddenly begin to notice how cool she is.

"Child Abduction is Not Funny" 
Numerous news reports about missing children in other cities incite panic among South Park parents.

"A Ladder to Heaven"   
After realizing that Kenny was the one with their candy shopping spree raffle ticket before he died, the boys construct a ladder leading to heaven in an attempt to find out from Kenny the location of the ticket.

"The Return of the Fellowship of the Ring to the Two Towers"   
A mix-up lands a "Lord of the Rings" video tape with Randy and Sharon Marsh, and a hardcore porno tape with the boys.

"The Death Camp of Tolerance"  
Mr. Garrison, newly promoted to fourth-grade teacher, attempts to use his homosexuality to get fired so he can sue the school for a substantial sum of money. The students' disgust with Garrison's outrageously inappropriate behavior with his new partner Mr. Slave incurs the anger of their parents, who attempt to teach their children to be tolerant of homosexuals.

"The Biggest Douche in the Universe"   
After the events in "A Ladder to Heaven", in which Cartman drinks Kenny's soul, Cartman becomes sick and travels with the boys and Chef to have Kenny's spirit exorcised. Stan has a run-in with famous TV "psychic" John Edward.

"My Future Self n' Me" 
Stan is suspicious when an alcoholic, drug-addicted future version of himself "travels back" in time and meets him.

"Red Sleigh Down"  
Cartman, concerned about being on Santa's "naughty list", takes Stan and Kyle on a mission to bring Christmas to a war-torn Iraq.

"Cancelled"
The boys learn that Earth is a reality show for aliens and must save it from cancellation.

"Krazy Kripples"
Timmy and Jimmy start a club for cripples. Christopher Reeve comes to town to promote stem cell research.

"Toilet Paper"
Kyle feels guilty after he and the boys TP their art teacher's house.

"I'm a Little Bit Country"
The boys enter an anti-war demonstration; Cartman travels back in time to the American Revolutionary War era.

"Fat Butt and Pancake Head"    
Cartman's hand puppet Jennifer Lopez gets major publicity, which angers the real Jennifer Lopez.

"Lil' Crime Stoppers"  
The boys pretend to be police detectives.

"Red Man's Greed"
The town is taken over by Native Americans who want to create a highway.

"South Park is Gay!"   
The men and boys of town become metrosexual.

"Christian Rock Hard"  
Cartman, Token, and Butters form a Christian music band. Stan, Kyle, and Kenny learn about downloading free music off the Internet.

"Grey Dawn"    
The elderly have their driver's licenses taken away, against which the AARP retaliates.

"Casa Bonita"
Cartman tries to get himself invited to Kyle's birthday party at Casa Bonita, a Disneyland-like Mexican restaurant.

"All About Mormons"
Stan befriends a boy and his family, who are all Mormons.

"Butt Out"
The town calls in Rob Reiner to combat the spread of smoking among children after the boys are caught doing so.

"Raisins"
The boys take Stan to Raisins, a Hooters-like restaurant after Wendy breaks up with him. Butters meets a girl who seems interested in him.

"It's Christmas in Canada"
Kyle and the boys fly to Canada during Christmastime to see the Canadian Prime Minister after Ike's biological parents take him back to Canada.

"Good Times with Weapons"
The boys buy weapons at a fair and imagine themselves as anime characters.

"Up the Down Steroid"
Jimmy uses steroids to cheat in the Special Olympics. Cartman disguises himself as being mentally retarded to win the prize.

"The Passion of the Jew"
Kyle develops feelings of anti-Semitism after watching Mel Gibson's The Passion of the Christ.

"You Got F'd in the A"
Stan must form a dance group to compete against rivals from Orange County in a spoof of You Got Served.

"AWESOM-O"
Cartman pretends to be a robot so he can hear private secrets from Butters.

"The Jeffersons"
All the children want to be friends with a rich new neighbor who is under investigation by the police.

"Goobacks"
The town becomes angry when immigrants from the year 3045 arrive and take the residents' jobs for lower wages.

"Douche and Turd"
Stan is forced to vote in an election for the school's new mascot.

"Something Wall-Mart This Way Comes"
When a Wall-Mart store comes to South Park, all the independent stores go out of business.

"Pre-School"
A face from the past causes trouble for the boys.

"Quest for Ratings"    
The boys' school news show is in competition against a rival television program created by Craig.

"Stupid Spoiled Whore Video Playset"
Wendy feels left out when all the fourth grade girls start acting like Paris Hilton.

"Cartman's Incredible Gift"
Cartman gains paranormal powers and uses them to become a psychic detective for hire.

"Woodland Critter Christmas"
Stan helps the Woodland Critters, who await the birth of their savior.

"Mr. Garrison's Fancy New Vagina"
A sex change turns Mr. Garrison into "Mrs. Garrison".

"Die Hippie, Die"
Cartman seeks to rid South Park of its growing hippie population. Stan, Kyle, and Kenny become more like hippies.

"Wing"
The boys start a talent agency in hopes of making money from Token.

"Best Friends Forever"
Kenny is killed by heaven after becoming master of the PSP, but the town brings him back to life; leaving him in a persistent vegetative state.

"The Losing Edge"
The boys try to lose their baseball games on purpose so they can avoid playing all summer. Randy gets into training to fight the other fathers at the games.

"The Death of Eric Cartman"
The kids of South Park agree to ignore Cartman, leading him to think that he is dead.

"Erection Day"
Jimmy starts getting erections and worries about performing in the school talent show.

"Two Days Before the Day After Tomorrow"
A state of emergency is declared in South Park after it is announced that global warming is coming.

"Marjorine"
Butters is forced to fake his own death in order to snoop in on the girls' sleepover as Marjorine, the new girl.

"Follow That Egg!"
After learning Mr. Slave will marry Big Gay Al, Mrs. Garrison vows to stop same-sex marriage from being approved. A project involving an egg makes Stan and Kyle into rivals.

"Ginger Kids"
Cartman suffers from a mysterious and sudden onset of the 'disease' Gingervitis. He then starts a campaign to give children in his assumed position "more than equal" rights.

"Trapped in the Closet"
Stan looks to a new religion for answers. Tom Cruise, R. Kelly, and John Travolta lock themselves in Stan's closet.

"Free Willzyx"
A "talking" whale inspires the boys to risk everything to "return him to his family on the moon".

"Bloody Mary"
Randy's drinking problem reaches its peak. A Virgin Mary statue in a neighboring town begins to bleed from its rectum.

"The Return of Chef"
Chef leaves South Park to join the "Super Adventure Club". When he returns, the boys notice there's something wrong with him.

"Smug Alert!"  
Stan persuades everyone in town to buy hybrid cars, not realizing the new cars cause a different kind of dangerous emission.

"Cartoon Wars Part I"  
The town is in panic when Family Guy angers the Muslim world by attempting to air an image of Mohammed. Kyle agrees to help Cartman have the next uncensored episode pulled.

"Cartoon Wars Part II" 
Cartman meets with the president of FOX in an attempt to cancel Family Guy.

"A Million Little Fibers"
Broke and needing to pay for his rent, Towelie gets high and decides to publish his memoirs. However, every time he gets high, something goes wrong.

"ManBearPig"
Al Gore gets the boys trapped in the Cave Of The Winds while trying to kill the purported "Manbearpig".

"Tsst"
When Cartman's mom realizes she can't control her son anymore, she gets help from an expert.

"Make Love, Not Warcraft"
The boys dedicate their lives to defeat a mad gamer, and save the World of Warcraft.

"Mystery of the Urinal Deuce"
Cartman "discovers" the true culprit behind the 9/11 attacks. Mr. Mackey is determined to find out who defecated in the urinal at South Park Elementary.

"Miss Teacher Bangs a Boy" 
A South Park Elementary School teacher is conducting an illicit affair with a student. As the new School Hallway Monitor, Cartman takes it personally when an infraction is committed in his jurisdiction.

"Hell on Earth 2006"
Satan decides to throw a big party on Earth, but has trouble deciding who to invite. He wants to invite lots of celebrities that are alive, but is running out of room for his friends.

"Go God Go"
Cartman, unable to wait for the Nintendo Wii, freezes himself until it is released. After an avalanche he becomes trapped and wakes up in the future. Ms. Garrison meets Richard Dawkins.

"Go God Go XII"
Cartman tries to escape from the future while the war rages on between the Atheist factions.

"Stanley's Cup"
Stan's bike is towed that he needs for his paper route. To get it back he is forced to coach a pee-wee hockey team

"With Apologies to Jesse Jackson"
Randy says n*ggers on Wheel of Fortune and Cartman gets into a fight with a midget.

"Cartman Sucks"    
Cartman pulls his "best trick ever" on Butters and gets him put in a special camp where they "pray the gay away".

"Lice Capades"
A hair lice infection hits South Park Elementary. Can Clyde hide his terrible discovery from the others?

"The Snuke"
Hillary Clinton's campaign rally arrives in town. Cartman suspects a terrorist threat from the new Muslim student.

"Fantastic Easter Special" 
Stan wonders how Easter Eggs and Jesus dying on the cross are linked. He soon falls in with an eccentric society guarding a timeless secret.

"D-Yikes!"
Ms. Garrison gets dumped yet again, and lets her anger out on her fourth grade class.

"Night of the Living Homeless"
South Park is overrun with the homeless. The boys must figure out a way to get rid of them.

"Le Petit Tourette"
Cartman discovers the joys of having Tourette's syndrome.

"More Crap"
Randy becomes a town hero when everyone sees the size of his crap.

"Imaginationland Episode I"    
Kyle regrets making a bet with Cartman, and the boys enter a mysterious land full of imaginary creatures.

"Imaginationland, Episode II"
Cartman is determined to find Kyle while Butters remains trapped in Imaginationland as the evil creatures break through the barrier...

"Imaginationland, Episode III" 
Stan and Butters prepare for the battle of their lives, while Cartman takes his case to the Supreme Court.

"Guitar Queer-O"
Stan and Kyle become hooked on guitar hero, but Stan's superior skill threatens his and Kyle's friendship.

"The List" 
The boys try to obtain the list that the girls have made rating how attractive the boys are.

"Tonsil Trouble"
Cartman has his tonsils removed but is accidentally given HIV as a result of a blood transfusion.

"Britney's New Look"
The boys travel with Britney Spears to the North Pole and discover the secret of her popularity.

"Major Boobage"
Kenny becomes addicted to the latest drug. To get people off this, Gerald proposes a ban on Cats.

"Canada on Strike" 
The head of the World Canadian Bureau leads the country into a long and painful strike.

"Eek, A Penis!"
Mrs. Garrison goes in search of a way of becoming a man while Cartman is left to substitute.

"Over Logging" 
Randy moves the Marsh family towards California after the internet has gone.

"Super Fun Time"   
Mr. Garrison's field trip turns into a dangerous situation when everyone is taken hostage, while Butters is forced by Cartman to accompany him to the nearby amusement park.

"The China Probrem"
Cartman must confront the Chinese alone while the American people are haunted by the memory of recent tragic events.

"Breast Cancer Show Ever"  
Wendy gets into trouble after threatening to beat Cartman after school.

"Pandemic" 
While the world struggles to contain the latest epedemic of epic proportions, the boys find a way to make money off of it.

"Pandemic 2: The Startling"    
Randy bravely documents the destruction whilst trying to save his family.

"About Last Night..."
All the president candidates aren't who they seem to be...

"Elementary School Musical"
The boys realize they aren't the cool kids anymore, while Stan realizes that he could lose Wendy if he doesn't get on board with the latest fad to hit South Park Elementary

"The Ungroundable" 
Butters is sure he's seen a Vampire at school but he can't get anyone to listen to him. Meanwhile, the Goth Kids are angry and frustrated when the other kids can't tell the difference between a Goth Kid and a Vampire Kid.

"The Ring"
Thinking it's his way into her heart and other body parts, Kenny takes his new girlfriend to a Jonas Brothers concert. His dream of taking their relationship to the next level is crushed with the Jonas Brothers giving them purity rings.

"The Coon"
The Coon rises from the trash and takes his place as a lone vigilante.

"Margaritaville"
The economy is making everyone's life difficult, but Randy has a solution.

"Eat, Pray, Queef"
There is a new television series which freaks the boys out, called The Queef Sisters.

"Fishsticks"
Cartman decides to help Jimmy with his comedy routine. Everyone loves the new joke they come up with. The joke starts to take off and it even hits all the late night talk shows. The boys are thrilled with how popular it's become until somebody tries to take all the credit.

"Pinewood Derby"
Randy is determined that Stan will win this year's Pinewood Derby. He comes up with a plan that will assure Stan a first place trophy.

"Fatbeard"
Butters and a small group of recruits join Cartman in his dream of living on skull island where they will frolic in crystal clear waterfalls and discover buried treasure. Cartman promises that paradise awaits if they can just get to Somalia.

"Dead Celebrities" 
Ike is being tormented by paranormal forces. Kyle brings in professional ghost hunters to help save his little brother.

"Butters' Bottom Bitch"
Butters is determined to get his first kiss so his friends won't make fun of him anymore.

"W.T.F."
The boys decide to take up wrestling.

"Whale Whores"
Stan joins the whale wars crew and fights against the Japanese protecting the world's whales and dolphins.

"The F Word"
The boys fight back against the loud and obnoxious Motorcycle Riders that are disrupting everyone in South Park.

"Dances with Smurfs"
Cartman takes over the morning announcements and uses his new position to attack Wendy.

"Pee"
The boys and Jimmy visit the "Pi Pi Waterland" and experience a urine catastrophe in a parody of 2012.

"Sexual Healing"
The nation's top scientists come together to put a stop to the recent phenomenon of rich, successful men who suddenly want to have sex with many, many women. After extensive testing, some of the fourth grade boys in South Park Elementary are diagnosed as sex addicts.

"The Tale of Scrotie McBoogerballs"
The boys are given a controversial book to read in school that both excites and inspires them to write one of their own. When the boys discover that Stan's mom has found their masterpiece, their new motivation is how they can stay out of trouble.

"Medicinal Fried Chicken"
Cartman's favorite restaurant has been shut down and replaced by a store that sells medicinal marijuana. Randy is desperate to get a prescription card to buy pot and Cartman will do anything to get his beloved fried chicken back.

"You Have 0 Friends"   
Kyle "friends" the wrong person on facebook and now all of his old friends are deserting him. His situation is desperate. Kyle looks for help from the one person who has always been there for him. Stan gets sucked into Facebook.

"200"
While on a school field trip, Stan accidentally insults Tom Cruise (again), which sets off a chain reaction of enraged celebrities. As a result, 200 previously ridiculed celebrities stand strong in a class action lawsuit against the town of South Park. This could be the thing that destroys South Park forever. So it is up to Stan to come with a plan to sort out this predicament or they are all doomed.

"201"
Angry celebrities, violent ginger kids and Mecha Streisand are about to destroy South Park and all anyone wants to know is, â€œWho is Eric Cartman's father?â€

"Crippled Summer"
Competition is the name of the game this summer. There is no time for Jimmy and his friends to slack off. They're working to be this year's champions at summer camp. Jimmy suits up and prepares to shred in the annual surfing contest. Meanwhile Towelie goes through drug therapy.

"Poor and Stupid"  
Cartman wants to race with the pros and he's ready to do whatever it takes to make it happen. He's afraid that no matter how hard he tries, he'll never reach the the level of the other NASCAR drivers. Working with Butters as his pit boss, Cartman pulls out all the stops to compete in the race of his life.

"It's a Jersey Thing"
New Jersey is rapidly taking over the nation, one state at a time and their next stop is South Park. As the Jerseyites spill into Colorado and approach South Park, Randy and the boys stand strong against the onslaught.

"Insheeption"
When he's sent to the school counselor to talk about his disorder, Stan realizes that he's not the only one who has a problem. When Mr. Mackey and Stan agree to surrender themselves to the hoarding experts, Stan gets a more than a glimpse of what it was like for Mr. Mackey in the 4th grade at South Park Elementary.

"Coon 2: Hindsight"
"Coon and Friends" set out to help the victims of BP's latest catastrophic drilling accident in the Gulf. Much to the Coon's dismay, another Super Hero gets there first.

"Mysterion Rises"
Led by Mysterion, Coon and Friends are working together to help the people in the Gulf who are at the mercy of the dark lord, Cthulhu. The Coon, scorned by his fellow super heroes and now working alone, is out for revenge.

"Coon vs. Coon & Friends"
Coon and Friends find themselves at the mercy of Cartman who now has the dark lord, Cthulhu, doing his bidding. Kenny wrestles with the curse of his super power through his alter ego, Mysterion.

"CrÃ¨me Fraiche"
Stan's life is a shambles both at home and in school. Randy's obsession with the Food Network Is changing everything. It even forces Sharon to explore a new interest of her own.

"HUMANCENTiPAD"
Kyle is intimately involved in the development of a revolutionary new product that is about to be launched by Apple. Meanwhile, Cartman doesn't even have a regular iPad yet. He blames his mother.

"Funnybot"
At the schools first annual Comedy Awards, Jimmy announces that the Germans are the least funny people in the world. Germany is highly insulted. They vow that retaliation toward the kids at South Park Elementary will be swift and brutal.

"Royal Pudding"
It is a joyous time for all Canadians as the royal wedding commences. But just as the prince and princess are about to be joined for all eternity, the princess is abducted! All Canadians are called upon to help save the princess. Ike answers the call to arms.

"T.M.I."
Cartman is furious when the school posts the kids' penis sizes on the bulletin board. He throws an absolute fit and once again finds himself in the principal's office. This time he gets sent to anger management therapy.

"Crack Baby Athletic Association"
Kyle gets in on the ground floor of Cartman's latest business venture, The Crack Baby Athletic Association.

"City Sushi"
Butters is taken to a psychiatrist who claims that he has Multiple Personality Disorder, in which he needs medication for. Meanwhile, a new restaurant opens next to South Park's City Wok.

"You're Getting Old"
After Stan celebrates his 10th birthday, he begins to see everything differently. The other boys think he's become a major buzzkill and start to avoid hanging out with him. When Stan and Kyle have a major blow up, the very fabric of South Park begins to unravel.

"Ass Burgers"
Cartman tries to give himself Asperger's Syndrome in an unusual way. Meanwhile, Stan doesn't seem to be able to get his life back to normal no matter what he tries.

"The Last of the Meheecans"
Butters ends up living in Mexico. When several mexicans believe it is best to cross over to Mexico, Cartman joins the Border Patrol.

"Bass to Mouth"
The students of South Park Elementary are the victims of a new gossip website. An elusive hacker has somehow gained access into the student's confidential phone calls and e-mails and is posting all their juicy stories. The boys are shocked when they discover the identity of the hacker.

"Broadway Bro Down"
Sharon is thrilled that Randy is making an effort to do more things that she enjoys. But, after he takes her to see a hit musical in Denver, Randy becomes Broadway's biggest fan. Sharon is whisked away to New York and treated to every musical on the Great White Way.

"1%"
The kids at South Park Elementary are being punished for Cartman's failings in the physical education department. What will Cartman do when they all gang up on him?

"A History Channel Thanksgiving"
After watching a Thanksgiving special on The History Channel, the boys believe that aliens were involved in the original feast. But, questions remain... was the first Thanksgiving haunted? Is alien technology responsible for stuffing? The truth could change Thanksgiving for everyone.

"The Poor Kid"
When Kenny's parents are arrested, the McCormick kids are put in an agnostic foster home. Cartman finds out he is the second poorest kid and attempts to get himself put in a foster home on Hawaii; this plan backfires. Cartman ends up living with Kenny where he or Kenny are no longer the "poor kids".

"Reverse Cowgirl"
When one of the boys leaves the toilet seat up after he uses the bathroom, an unspeakable tragedy occurs.

"Cash For Gold"
Cartman launches his own gem shopping channel.

"Faith Hilling"
The kids are in danger when new trends start to evolve and shift at a rapid pace.

"Jewpacabra"
The town's big Easter Egg Hunt is in jeopardy when Cartman produces video evidence of a mysterious creature lurking in the woods.

"Butterballs"
Butters is the victim of an unlikely bully.

"I Should Have Never Gone Ziplining"
The boys' ziplining adventure becomes a terrifying test of survival.

"Cartman Finds Love"
The time has finally come for Cartman to let a special someone know exactly how he feels.

"Sarcastaball"
South Park Elementary takes steps to address football's concussion crisis.

"Raising the Bar"
Cartman finally admits he's fat and immediately gets a mobility scooter.

"Insecurity"
Cartman signs up for a home security system.

"Going Native"
It is time for Butters to begin a journey where he will follow in the path of his Hawaiian ancestors.

"A Nightmare on Face Time"
Randy's big plans for Halloween night keep Stan from trick or treating with his friends.

"A Scause For Applause"
A serious doping scandal shakes everyone's faith in a beloved icon. Everyone who once supported the fallen hero is now cutting off their symbolic yellow wristbands.

"Obama Wins!"
Eric Cartman is hiding something in his bedroom that could change the entire outcome of the Presidential election.

"Let Go, Let Gov"
Cartman infiltrates the NSA and doesn't like what he finds in his personal file.

"Informative Murder Porn"  
The boys use the game of Minecraft as a distraction to keep their parents from hurting each other.

"World War Zimmerman"  
Cartman sees Token as a threat to all humanity.

"Goth Kids 3: Dawn of the Posers"  
The Goth Kids are being sent away to a camp for troubled children.

"Taming Strange"   
When Ike hits puberty, he and Kyle start to grow apart. To save their relationship, Kyle takes Ike to see a live performance of Yo Gabba Gabba!.

"Ginger Cow"   
Cartman's latest prank brings peace to the world.

"Black Friday"
The boys prepare to battle the crowds already lining up for the first official day of holiday shopping.

"A Song of Ass and Fire"   
Black Friday is almost here and the battle for the new gaming devices is heating up. Princess Kenny's betrayal has left Cartman out for revenge.

"Titties and Dragons"  
The doors to the mall will finally open for the biggest Black Friday sale in history. The boys are divided over which gaming device to buy and a bloody battle will determine whether Xbox or Sony will be the winner.

"The Hobbit"   
When Wendy tries to fix one of her girlfriends up with Butters, she ends up in the counselor's office.

"Go Fund Yourself"
The boys name their new start-up company, The Washington Redskins.

"Gluten Free Ebola"
South Park goes gluten free.

"The Cissy"
Randy is harboring a giant secret and the pressure is getting to him. Meanwhile, Cartman calls Stan a cissy.

"Handicar"
Timmy's successful new car service makes him a lot of enemies.

"The Magic Bush"
Graphic video from an unknown drone is uploaded on the internet.

"Freemium Isn't Free"
Stan is addicted to the new Terrance and Phillip mobile game.

"Grounded Vindaloop"
Butters is convinced he's living in a virtual reality.

"Cock Magic"
There are illegal goings-on in the basement of City Wok.

"#REHASH"
Kyle just wants to play video games with his little brother. But, when Ike doesn't want to play with him anymore, Kyle is afraid that the next generation is passing him by.

"#HappyHolograms"
CartmanBrah is trending as the country prepares to watch the biggest Holiday Spectacular ever.

"Stunning and Brave"
There is a new principal at the helm of South Park Elementary. He forces the boys to confront the damage they've done through their history of racism and unconscious bias. It is the most stunning and brave South Park ever.

"Where My Country Gone?"   
Garrison wants to build a wall to keep out all of the undocumented immigrants.

"The City Part of Town"
The town of South Park is gentrifying, Kenny gets a job at City Wok.

"You're Not Yelping"
A new Mexican restaurant opens in South Park and Eric Cartman will give his expert advice to the owner.

"Safe Space"
Randy has to deal with uncomfortable confrontations every time he shops at the new Whole Foods. He feels exposed at every turn and it's ruining his Whole Foods experience. Randy and Cartman are both seeking a safe space.

"Tweek x Craig"
The news of a romantic relationship between Tweek and Craig hits South Park Elementary. Meanwhile, Cartman, who struggles to understand his friends' relationship, finds he has an admirer of his own.

"Naughty Ninjas"   
When Kenny leads the boys in playing Ninja Warriors, a foreign terrorist organization takes notice.

"Sponsored Content"
Jimmy is sent to the principal's office for using an inappropriate word in the school paper. His integrity as a newsman runs head on into PC Principals ideology. Will Jimmy be the undoing of PC Principal?

"Truth and Advertising"
Being the crack reporter that he is, Jimmy sets out to learn everything he can about what makes Leslie tick. Meanwhile, Principal Victoria and Mr. Garrison return to a South Park that has become unrecognizable.

"PC Principal Final Justice"
The gentrification of South Park is pricing Randy right out of town. Meanwhile, Kyle's distrust of Stan has broken their friendship and thrown Kyle into a dangerous alliance.

"Member Berries"
Mr. Garrison is still on the campaign trail as the National Anthem gets a reboot by an American Icon.

"Skank Hunt"
The boys decide they have to take down Cartman but meanwhile, Skank Hunt takes his rein of terror global.

"The Damned"
Gerald is thrilled with the media attention as he continues to troll everyone and anyone.

"Wieners Out"
Kyle feels tremendous guilt over the rift between the boys and the girls. When he tries to bring them together, things only get worse. The boys finally band together to stand up for their rights.

"Douche and a Danish"
The kids get pulled in to the search for the notorious Skankhunt42. Meanwhile, Gerald joins forces with the other trolls to stop Denmark from launching TrollTrace.com.

"Fort Collins"
An entire city in Colorado gets hacked. Gerald and Cartman may lose everything when their complete history of internet activity becomes public.

"Oh, Jeez"
PC Principal tries one more time to make peace between the boys and the girls. Meanwhile Gerald comes face-to-face with the Troll Hunter.

"Members Only"
Gerald tries anything to escape the Troll Hunter's revenge. Meanwhile, Cartman and Heidi make their way to SpaceX to try to get on the first rocket leaving for Mars.

"Not Funny"
Cartman is certain Heidi can solve the problem of getting them to Mars because she's really funny. Gerald tries to save himself by reasoning with the Troll Hunter while Garrison explores his new found military power.

"The End of Serialization as We Know It"
As TROLLTRACE goes live, Sheila logs on to see Gerald's on-line activity. At SpaceX, Cartman tries to convince the scientists that going to Mars is a bad idea. And defying their mom, Kyle and Ike get all the kids together to try to save the world from certain destruction..

"White People Renovating Houses"
Randy comes to grips with what it means to be white in today's society.

"Put It Down"
When Tweek is caught in the middle of a petty conflict, it drives his relationship with Craig to the brink.

"Holiday Special"
In a return to form, a forbidden love story between a white man and a Native American man unfolds.

"Franchise Prequel"    
Facebook is the ultimate weapon for Professor Chaos.

"Hummels & Heroin"
Beloved entertainers are being cut down in their prime due to massive overdoses of opiates. Stan is about to be exposed as the source of the illegal drugs.

"Sons A Witches"
At the annual Halloween get together, a witch casts a spell that terrorizes everyone in South Park.

"Doubling Down"
Kyle is playing with fire when he gets in the middle of Cartman and Heidi's relationship.

"Moss Piglets" 
Jimmy and Timmy's experiment could win them first prize in the annual science fair.

"SUPER HARD PCness"
It's never been more challenging to be a PC Principal.

"Splatty Tomato"
The children of South Park claim to have seen Mr. Garrison lurking around town. The townspeople are angry that the President is scaring their children.

"Dead Kids"
Randy is desperate to help Sharon get her emotions under control and Cartman unexpectedly fails his math test.

"A Boy And A Priest"
A very special relationship has developed between Butters and the Parish Priest. When the town finds the church doors locked and no sign of the pair, they call in the Catholic Church

"The Problem with a Poo"   
Mr. Hankey's offensive behavior puts him in jeopardy of being fired as the Director of the Annual Christmas Pageant.

"Tegridy Farms"
Butters is selling vape pens and all kinds of fruity-flavored vape accessories at school. Meanwhile, Randy decides he should move the family to the country and take up farming.

"The Scoots"
The kids plan to use the latest revolution in mobility to get more candy on Halloween than they have ever gotten before.

"Time To Get Cereal"
When dead citizens start popping up all over town, the boys realize they need Al Gore's help. The boys are willing to do almost anything to save the town, and themselves, but it may be just too late.

"Nobody Got Cereal?"
The boys break out of jail and are on the run from the police and ManBearPig.

"Buddha Box"
Cartman just can't deal with people any longer. They get in the way of what's most important in his life.

"Unfulfilled"
The citizens of South Park are enjoying all the perks of being a company town when the Amazon Fulfillment Center moves in. Everything is just swell until the contradictions inherent in capitalism threaten to bring down the entire system down.

"Bike Parade"
Despite the chaos at the Amazon Fulfillment Center, the Bike Parade is still on. The boys' chance of winning is in jeopardy when Kenny resists commercialism in solidarity with the striking workers.

"Mexican Joker"    
In the pilot episode of the new hit series, Tegridy Farms, Randy battles home-grown weed and comes to terms with the fact that he might be a towel. Meanwhile, Kyle goes to camp.

"Band in China"
Randy lands himself in big trouble on a visit to China. Meanwhile, Stan starts a band to work out his frustration over having to move away from South Park.

"Shots!!!"
This week, Randy revels in a Tegridy Farms milestone. Meanwhile, Cartman stands his ground and refuses to get a shot.

"Let Them Eat Goo"
The citizens of South Park are moving toward a completely plant-based diet. Cartman is pretty sure the new food in the cafeteria gave him a heart attack.

"Tegridy Farms Halloween Special"
It's Halloween and Randy is dealing with his daughter's marijuana problem. Butters gets an unexpected surprise when he visits the Egyptian Artifact exhibit at the Denver Museum.

"Season Finale"
The Mayor has evidence that Randy blew up his neighbor's yards in protest over homegrown weed and then blamed it on a Mexican Joker. Now the citizens of South Park have had enough of Randy and Tegridy Farms and they just want to lock him up.

"Board Girls"
In the season opener, an even stronger woman causes big problems for PC Principal. Cartman, Stan, and the rest of the boys meet their match when some of the girls join their board gamers club.

"Turd Burglars"
Kyle's mom looks so good after her fecal transplant that everyone wants to get their hands on her goods. Cartman and the boys jump into the quest for the best microbiome.

"Basic Cable"
Scott Malkinson's future with the new girl in his class depends on him getting the latest and greatest streaming platform. Scott's dad works for the local cable company and refuses to move beyond basic cable.

"Christmas Snow"
It's a bleak Christmas Season in South Park this year and it's all Santa's fault. He is single handedly stealing the joy from the holiday. The town just wants their Christmas Spirit back but that will take a Christmas miracle.

"The Pandemic Special"
Randy comes to terms with his role in the COVID-19 outbreak as the on-going pandemic presents continued challenges to the citizens of South Park. The kids happily head back to school but nothing resembles the normal that they once knew; not their teachers, not their homeroom, not even Eric Cartman.

"South ParQ Vaccination Special"
The citizens of South ParQ are clamoring for the COVID-19 vaccine. A hilarious new militant group tries to stop the boys from getting their teacher vaccinated.
"""
categories = [south_park]
categories_name = ["South Park"]

for i in range(len(categories)):
    categories[i] = categories[i].split("\n\n")

df = pd.DataFrame(columns=['sentence', 'category'])

for i in range(len(categories_name)):
    for j in range(len(categories[i])):
        df = df.append({'sentence': categories[i][j], 'category': categories_name[i]}, ignore_index=True)

    df = df[df['sentence'] != ""]
    df.reset_index(drop=True, inplace=True)

df["sentence_c"] = df['sentence'].copy()

for i in range(len(df)):
    df["sentence_c"][i] = re.sub('[!@#â€™â€˜?.,\'$]', '', df["sentence_c"][i])
    df["sentence_c"][i] = df["sentence_c"][i].lower()

#streamlit
st.sidebar.header("southparksouthparsouthpark")
st.sidebar.write("south park random episode simulator")
st.title("MR MACKEY FOUND RANDOM SOUTH PARK EPISODES FOR YOU, M'KAY")
st.image("https://c.tenor.com/5q1Ly0am-MAAAAAC/mmmkay-mr-mackey.gif", width=750)
st.header("I'M GOING DOWN TO SOUTH PARK, GONNA HAVE MYSELF A TIME")
st.image("https://www.nicepng.com/png/full/149-1498488_south-park-transparent-png-images-stan-marsh-kyle.png", width=750)
st.image("https://giffiles.alphacoders.com/311/3117.gif", width=750)
st.image("https://labgif.com/wp-content/uploads/2021/04/73081.gif", width=750)
st.image("https://giffiles.alphacoders.com/999/9998.gif", width=750)
st.image("http://media3.giphy.com/media/3osxYxC0sdkbz9fPvW/giphy.gif", width=750)
st.image("https://galeri13.uludagsozluk.com/660/obez-yazarlarin-gobegi_1474404.gif", width=750)
st.image("https://i.pinimg.com/originals/9d/35/c8/9d35c8cea25c36035d4f00e662e09d69.gif", width=750)
st.image("https://2.bp.blogspot.com/-ZooLAjM4Sls/Wh8Hg2AUt2I/AAAAAAAAfpw/2mxSAw2_9qEGXQ8T4ZIoSHuBt5ttqF7IACLcBGAs/s1600/giphy-4.gif", width=750)
st.image("http://s3.amazonaws.com/blogs.comedycentral.com-production/wp-content/uploads/sites/58/2014/09/1801_13.gif", width=750)
st.image("https://media.giphy.com/media/xT1R9J2v6hnFxTFjEY/giphy.gif", width=750)
st.image("https://i.gifer.com/1M4h.gif", width=750)
st.image("https://giffiles.alphacoders.com/212/212301.gif", width=750)

user_input = st.sidebar.text_input("TYPE HERE WHAT YOU WANT FROM THE EPISODE")
st.sidebar.write(random_jaccard_recommandation(re.sub('[!@#â€™â€˜?.,\'$]', '', str(user_input).lower())))
