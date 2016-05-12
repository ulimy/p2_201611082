def h1():
    AllData=list()
    AllData=[[13.1,37.1,39.6,8.7,1.5],
    [10.6,34.6,39.5,13.4,1.9],
    [27.1,40.0,28.5,2.9,1.5],
    [16.2,37.8,38.4,6.8,0.8],
    [11.4,29.8,39.0,14.8,4.9],
    [12.2,26.5,42.0,14.9,4.4],
    [13.5,29.7,43.4,11.1,2.4],
    [13.7,37.6,43.4,4.1,1.2]]
    goodsum=0
    badsum=0
    for i in AllData:
        goodsum=goodsum+i[0]+i[1]
    goodaverage=goodsum/len(AllData)
    for i in AllData:
        badsum=badsum+i[2]+i[3]
    badaverage=badsum/len(AllData)
    print ("goodaverage: ",goodaverage)
    print ("badaverage: ",badaverage)
def h2():
    speech1=list()
    speech1=["Vice President Cheney, Mr. Chief Justice, President Carter, President Bush, President Clinton, reverend clergy, distinguished guests, fellow citizens:" 

    "On this day, prescribed by law and marked by ceremony, we celebrate the durable wisdom of our Constitution, and recall the deep commitments that unite our country. I am grateful for the honor of this hour, mindful of the consequential times in which we live, and determined to fulfill the oath that I have sworn and you have witnessed.",

    "At this second gathering, our duties are defined not by the words I use, but by the history we have seen together. For a half century, America defended our own freedom by standing watch on distant borders. After the shipwreck of communism came years of relative quiet, years of repose, years of sabbatical —and then there came a day of fire. ",

    "We have seen our vulnerability —and we have seen its deepest source. For as long as whole regions of the world simmer in resentment and tyranny —prone to ideologies that feed hatred and excuse murder — violence will gather, and multiply in destructive power, and cross the most defended borders, and raise a mortal threat. There is only one force of history that can break the reign of hatred and resentment, and expose the pretensions of tyrants, and reward the hopes of the decent and tolerant, and that is the force of human freedom. ",

    "We are led, by events and common sense, to one conclusion: The survival of liberty in our land increasingly depends on the success of liberty in other lands. The best hope for peace in our world is the expansion of freedom in all the world.",

    "America's vital interests and our deepest beliefs are now one. From the day of our Founding, we have proclaimed that every man and woman on this earth has rights, and dignity, and matchless value, because they bear the image of the Maker of Heaven and earth. Across the generations we have proclaimed the imperative of self-government, because no one is fit to be a master, and no one deserves to be a slave. Advancing these ideals is the mission that created our Nation. It is the honorable achievement of our fathers. Now it is the urgent requirement of our nation's security, and the calling of our time. ",

    "So it is the policy of the United States to seek and support the growth of democratic movements and institutions in every nation and culture, with the ultimate goal of ending tyranny in our world. ",

    "This is not primarily the task of arms, though we will defend ourselves and our friends by force of arms when necessary. Freedom, by its nature, must be chosen, and defended by citizens, and sustained by the rule of law and the protection of minorities. And when the soul of a nation finally speaks, the institutions that arise may reflect customs and traditions very different from our own. America will not impose our own style of government on the unwilling. Our goal instead is to help others find their own voice, attain their own freedom, and make their own way. ",

    "The great objective of ending tyranny is the concentrated work of generations. The difficulty of the task is no excuse for avoiding it. America's influence is not unlimited, but fortunately for the oppressed, America's influence is considerable, and we will use it confidently in freedom's cause.",

    "My most solemn duty is to protect this nation and its people against further attacks and emerging threats. Some have unwisely chosen to test America's resolve, and have found it firm.",

    "We will persistently clarify the choice before every ruler and every nation: The moral choice between oppression, which is always wrong, and freedom, which is eternally right. America will not pretend that jailed dissidents prefer their chains, or that women welcome humiliation and servitude, or that any human being aspires to live at the mercy of bullies.",

    "We will encourage reform in other governments by making clear that success in our relations will require the decent treatment of their own people. America's belief in human dignity will guide our policies, yet rights must be more than the grudging concessions of dictators; they are secured by free dissent and the participation of the governed. In the long run, there is no justice without freedom, and there can be no human rights without human liberty. ",

    "Some, I know, have questioned the global appeal of liberty —though this time in history, four decades defined by the swiftest advance of freedom ever seen, is an odd time for doubt. Americans, of all people, should never be surprised by the power of our ideals. Eventually, the call of freedom comes to every mind and every soul. We do not accept the existence of permanent tyranny because we do not accept the possibility of permanent slavery. Liberty will come to those who love it. ",

    "Today, America speaks anew to the peoples of the world: ",

    "All who live in tyranny and hopelessness can know: the United States will not ignore your oppression, or excuse your oppressors. When you stand for your liberty, we will stand with you. ",

    "Democratic reformers facing repression, prison, or exile can know: America sees you for who you are: the future leaders of your free country. ",

    "The rulers of outlaw regimes can know that we still believe as Abraham Lincoln did: Those who deny freedom to others deserve it not for themselves; and, under the rule of a just God, cannot long retain it ",

    "The leaders of governments with long habits of control need to know: To serve your people you must learn to trust them. Start on this journey of progress and justice, and America will walk at your side. ",

    "And all the allies of the United States can know: we honor your friendship, we rely on your counsel, and we depend on your help. Division among free nations is a primary goal of freedom's enemies. The concerted effort of free nations to promote democracy is a prelude to our enemies' defeat. ",

    "Today, I also speak anew to my fellow citizens: ",

    "From all of you, I have asked patience in the hard task of securing America, which you have granted in good measure. Our country has accepted obligations that are difficult to fulfill, and would be dishonorable to abandon. Yet because we have acted in the great liberating tradition of this nation, tens of millions have achieved their freedom. And as hope kindles hope, millions more will find it. By our efforts, we have lit a fire as well —a fire in the minds of men. It warms those who feel its power, it burns those who fight its progress, and one day this untamed fire of freedom will reach the darkest corners of our world. ",

    "A few Americans have accepted the hardest duties in this cause —in the quiet work of intelligence and diplomacy ... the idealistic work of helping raise up free governments ... the dangerous and necessary work of fighting our enemies. Some have shown their devotion to our country in deaths that honored their whole lives —and we will always honor their names and their sacrifice. ",

    "All Americans have witnessed this idealism, and some for the first time. I ask our youngest citizens to believe the evidence of your eyes. You have seen duty and allegiance in the determined faces of our soldiers. You have seen that life is fragile, and evil is real, and courage triumphs. Make the choice to serve in a cause larger than your wants, larger than yourself —and in your days you will add not just to the wealth of our country, but to its character. ",

    "America has need of idealism and courage, because we have essential work at home —the unfinished work of American freedom. In a world moving toward liberty, we are determined to show the meaning and promise of liberty. ",

    "In America's ideal of freedom, citizens find the dignity and security of economic independence, instead of laboring on the edge of subsistence. This is the broader definition of liberty that motivated the Homestead Act, the Social Security Act, and the G.I. Bill of Rights. And now we will extend this vision by reforming great institutions to serve the needs of our time. To give every American a stake in the promise and future of our country, we will bring the highest standards to our schools, and build an ownership society. We will widen the ownership of homes and businesses, retirement savings and health insurance —preparing our people for the challenges of life in a free society. By making every citizen an agent of his or her own destiny, we will give our fellow Americans greater freedom from want and fear, and make our society more prosperous and just and equal.", 

    "In America's ideal of freedom, the public interest depends on private character —on integrity, and tolerance toward others, and the rule of conscience in our own lives. Self-government relies, in the end, on the governing of the self. That edifice of character is built in families, supported by communities with standards, and sustained in our national life by the truths of Sinai, the Sermon on the Mount, the words of the Koran, and the varied faiths of our people. Americans move forward in every generation by reaffirming all that is good and true that came before —ideals of justice and conduct that are the same yesterday, today, and forever. ",

    "In America's ideal of freedom, the exercise of rights is ennobled by service, and mercy, and a heart for the weak. Liberty for all does not mean independence from one another. Our nation relies on men and women who look after a neighbor and surround the lost with love. Americans, at our best, value the life we see in one another, and must always remember that even the unwanted have worth. And our country must abandon all the habits of racism, because we cannot carry the message of freedom and the baggage of bigotry at the same time. ",

    "From the perspective of a single day, including this day of dedication, the issues and questions before our country are many. From the viewpoint of centuries, the questions that come to us are narrowed and few. Did our generation advance the cause of freedom? And did our character bring credit to that cause? ",

    "These questions that judge us also unite us, because Americans of every party and background, Americans by choice and by birth, are bound to one another in the cause of freedom. We have known divisions, which must be healed to move forward in great purposes —and I will strive in good faith to heal them. Yet those divisions do not define America. We felt the unity and fellowship of our nation when freedom came under attack, and our response came like a single hand over a single heart. And we can feel that same unity and pride whenever America acts for good, and the victims of disaster are given hope, and the unjust encounter justice, and the captives are set free. ",

    "We go forward with complete confidence in the eventual triumph of freedom. Not because history runs on the wheels of inevitability; it is human choices that move events. Not because we consider ourselves a chosen nation; God moves and chooses as He wills. We have confidence because freedom is the permanent hope of mankind, the hunger in dark places, the longing of the soul. When our Founders declared a new order of the ages; when soldiers died in wave upon wave for a union based on liberty; when citizens marched in peaceful outrage under the banner Freedom Now —they were acting on an ancient hope that is meant to be fulfilled. History has an ebb and flow of justice, but history also has a visible direction, set by liberty and the Author of Liberty. ",

    "When the Declaration of Independence was first read in public and the Liberty Bell was sounded in celebration, a witness said, It rang as if it meant something. In our time it means something still. America, in this young century, proclaims liberty throughout all the world, and to all the inhabitants thereof. Renewed in our strength — tested, but not weary — we are ready for the greatest achievements in the history of freedom. ",

    "May God bless you, and may He watch over the United States of America. "
    ]
    speech2=list()
    speech2=[
    "CALLED upon to undertake the duties of the first executive office of our country, I avail myself of the presence of that portion of my fellow-citizens which is here assembled to express my grateful thanks for the favor with which they have been pleased to look toward me, to declare a sincere consciousness that the task is above my talents, and that I approach it with those anxious and awful presentiments which the greatness of the charge and the weakness of my powers so justly inspire.", 
    "A rising nation, spread over a wide and fruitful land, traversing all the seas with the rich productions of their industry, engaged in commerce with nations who feel power and forget right, advancing rapidly to destinies beyond the reach of mortal eye - when I contemplate these transcendent objects, and see the honor, the happiness, and the hopes of this beloved country committed to the issue, and the auspices of this day, I shrink from the contemplation, and humble myself before the magnitude of the undertaking.", 
    "Utterly, indeed, should I despair did not the presence of many whom I here see remind me that in the other high authorities provided by our Constitution I shall find resources of wisdom, of virtue, and of zeal on which to rely under all difficulties.",
    "To you, then, gentlemen, who are charged with the sovereign functions of legislation, and to those associated with you, I look with encouragement for that guidance and support which may enable us to steer with safety the vessel in which we are all embarked amidst the conflicting elements of a troubled world.",
    "During the contest of opinion through which we have passed the animation of discussions and of exertions has sometimes worn an aspect which might impose on strangers unused to think freely and to speak and to write what they think; but this being now decided by the voice of the nation, announced according to the rules of the Constitution, all will, of course, arrange themselves under the will of the law, and unite in common efforts for the common good.",
    "All, too, will bear in mind this sacred principle, that though the will of the majority is in all cases to prevail, that will to be rightful must be reasonable; that the minority possess their equal rights, which equal law must protect, and to violate would be oppression. Let us, then, fellow-citizens, unite with one heart and one mind. Let us restore to social intercourse that harmony and affection without which liberty and even life itself are but dreary things.",
    "And let us reflect that, having banished from our land that religious intolerance under which mankind so long bled and suffered, we have yet gained little if we countenance a political intolerance as despotic, as wicked, and capable of as bitter and bloody persecutions. During the throes and convulsions of the ancient world, during the agonizing spasms of infuriated man, seeking through blood and slaughter his long-lost liberty, it was not wonderful that the agitation of the billows should reach even this distant and peaceful shore;",
    "that this should be more felt and feared by some and less by others, and should divide opinions as to measures of safety. But every difference of opinion is not a difference of principle. We have called by different names brethren of the same principle. We are all Republicans, we are all Federalists. If there be any among us who would wish to dissolve this Union or to change its republican form, let them stand undisturbed as monuments of the safety with which error of opinion may be tolerated where reason is left free to combat it.",
    "I know, indeed, that some honest men fear that a republican government can not be strong, that this Government is not strong enough; but would the honest patriot, in the full tide of successful experiment, abandon a government which has so far kept us free and firm on the theoretic and visionary fear that this Government, the world's best hope, may by possibility want energy to preserve itself? I trust not. I believe this, on the contrary, the strongest Government on earth.",
    "I believe it the only one where every man, at the call of the law, would fly to the standard of the law, and would meet invasions of the public order as his own personal concern. Sometimes it is said that man can not be trusted with the government of himself. Can he, then, be trusted with the government of others? Or have we found angels in the forms of kings to govern him? Let history answer this question.",
    "Let us, then, with courage and confidence pursue our own Federal and Republican principles, our attachment to union and representative government. Kindly separated by nature and a wide ocean from the exterminating havoc of one quarter of the globe; too high-minded to endure the degradations of the others; possessing a chosen country, with room enough for our descendants to the thousandth and thousandth generation;",
    "entertaining a due sense of our equal right to the use of our own faculties, to the acquisitions of our own industry, to honor and confidence from our fellow-citizens, resulting not from birth, but from our actions and their sense of them; enlightened by a benign religion, professed, indeed, and practiced in various forms, yet all of them inculcating honesty, truth, temperance, gratitude, and the love of man; acknowledging and adoring an overruling Providence,",
    " which by all its dispensations proves that it delights in the happiness of man here and his greater happiness hereafter - with all these blessings, what more is necessary to make us a happy and a prosperous people? Still one thing more, fellow-citizens - a wise and frugal Government, which shall restrain men from injuring one another, shall leave them otherwise free to regulate their own pursuits of industry and improvement, and shall not take from the mouth of labor the bread it has earned.",
    "This is the sum of good government, and this is necessary to close the circle of our felicities.",
    "About to enter, fellow-citizens, on the exercise of duties which comprehend everything dear and valuable to you, it is proper you should understand what I deem the essential principles of our Government, and consequently those which ought to shape its Administration. I will compress them within the narrowest compass they will bear, stating the general principle, but not all its limitations. Equal and exact justice to all men, of whatever state or persuasion, religious or political; peace, commerce, ",
    "and honest friendship with all nations, entangling alliances with none; the support of the State governments in all their rights, as the most competent administrations for our domestic concerns and the surest bulwarks against antirepublican tendencies; the preservation of the General Government in its whole constitutional vigor, as the sheet anchor of our peace at home and safety abroad; a jealous care of the right of election by the people - a mild and safe corrective of abuses which are lopped by the sword of revolution ",
    "where peaceable remedies are unprovided; absolute acquiescence in the decisions of the majority, the vital principle of republics, from which is no appeal but to force, the vital principle and immediate parent of despotism; a well disciplined militia, our best reliance in peace and for the first moments of war, till regulars may relieve them; the supremacy of the civil over the military authority; economy in the public expense, that labor may be lightly burthened; the honest payment of our debts and sacred preservation",
    "of the public faith; encouragement of agriculture, and of commerce as its handmaid; the diffusion of information and arraignment of all abuses at the bar of the public reason; freedom of religion; freedom of the press, and freedom of person under the protection of the habeas corpus, and trial by juries impartially selected. These principles form the bright constellation which has gone before us and guided our steps through an age of revolution and reformation.",
    "The wisdom of our sages and blood of our heroes have been devoted to their attainment. They should be the creed of our political faith, the text of civic instruction, the touchstone by which to try the services of those we trust; and should we wander from them in moments of error or of alarm, let us hasten to retrace our steps and to regain the road which alone leads to peace, liberty, and safety.",
    "I repair, then, fellow-citizens, to the post you have assigned me. With experience enough in subordinate offices to have seen the difficulties of this the greatest of all, I have learnt to expect that it will rarely fall to the lot of imperfect man to retire from this station with the reputation and the favor which bring him into it. Without pretensions to that high confidence you reposed in our first and greatest revolutionary character,", 
    "whose preeminent services had entitled him to the first place in his country's love and destined for him the fairest page in the volume of faithful history, I ask so much confidence only as may give firmness and effect to the legal administration of your affairs. I shall often go wrong through defect of judgment. When right, I shall often be thought wrong by those whose positions will not command a view of the whole ground. I ask your indulgence for my own errors,",
    "which will never be intentional, and your support against the errors of others, who may condemn what they would not if seen in all its parts. The approbation implied by your suffrage is a great consolation to me for the past, and my future solicitude will be to retain the good opinion of those who have bestowed it in advance, to conciliate that of others by doing them all the good in my power, and to be instrumental to the happiness and freedom of all." 
    "Relying, then, on the patronage of your good will, I advance with obedience to the work, ready to retire from it whenever you become sensible how much better choice it is in your power to make. And may that Infinite Power which rules the destinies of the universe lead our councils to what is best, and give them a favorable issue for your peace and prosperity."
    ]
    d1=dict()
    for line in speech1:
        for c in line.split():
            if c not in d1:
                d1[c]=1
            else:
                d1[c]=d1[c]+1
    up23=list()
    for i in d1:
        if d1[i]>=23:
            up23.append(i)
    d2=dict()
    for line in speech2:
        for c in line.split():
            if c not in d2:
                d2[c]=1
            else:
                d2[c]=d2[c]+1
    up20=list()
    for i in d2:
        if d2[i]>=20:
            up20.append(i)
    print ("speech1: ",up23)
    print ("speech2: ",up20)
def lab11():
    h1()
    h2()
def main():
    lab11()