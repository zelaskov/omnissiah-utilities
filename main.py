from PyInquirer import prompt
from pyfiglet import Figlet
from repositories import list_repositories, open_project
from setup_local import install_packages

font = Figlet(font="digital")
greeetings = font.renderText('Praise the Omnissiah')
print('''

                                                                            ,..........
									 RRRRRRRRRRRRRRRRR
								       RRRRrrrrrrrrRRRRRRRRRR
								     RRRrrrrrrrrrrrrRRRRRRRRRRRR
            	  						    RRRrrrrrrrrrrrrrrRRRRRRRRRRRRR
								  RRRRrrrrrrrrrrrrrrrrRRRRRRRRRRRRRRR
								 RRRRrrrrrrrrrrrrrrrrrrRRRRRRRRRRRRRR
								RRRRrrrrrrrrrrrrrrrrrrrRRRRRRRRRRRRRRR
							        RRrrrrrrrrrrrrrrrrrrrrrRRRRRRRRRRRRRRR
							       RRRrrrrrrrrrrrrrrrrrrrrrRRRRrrrrRRRRRRR
							      RRRrr	 rrrrrrrrrrrrrrRRRRrrrrrRRrrrRR
							     RR		     rrrrrrrrrrrrRRrrrrrRRRrrrR
							     RR			rrrrrrrrrRRrrrrrRrrrRRR
							    Rr	 		   rrrrrrRRRrrrRRrrrrRR
							   Rrr    =======     ======   rrrRRrrrRrrrrrrrr
							  Rrr     =======     ======      rrrrrrrrrrrrrR
					uhhhh...	    RR                             rrrrrrrRRRRRR
				     can I Help you?	    Rr                              rrrrrRRRRRRRR
			 				    Rr                                rrrrRRRRRRR
							   Rrr                           .     rrrRRRRRRRR
							   Rrr                          GGG       rrrrRRRRR
							   Rr       GG              ..  GGG  G    rrrrrrrrrr
							   Rr      GG              GGGG GGG  G   rrrrrrrrrrr
							  Rr      GG               GGG\  GG  G  rrrrrrrrrrrr
							  R      GG   GGGg          GGG\ G   G  rrrrrrRrrrrr
							 R    R  GG  GGGg           GGGG     G  rrrrrrRrrrrr
						    ..... R   R  GG  GGg             GGGG   G  rrrRrrrrrRrrr
						  GGGGGG GGG    GG  GGg          g    GGG  G  rrrRrrrrrRrrrr
						 GGGGrrrGGGGrr  GG GGG           GG    GGG   rrrrrrrrrrrrrrr
					        rGGGGrrrGGGGrrr   GGg  g        GG      GGG  rrrrrrrrrrrrrrr
						rGGGrrrrrGGGrrr  GGG   g        GG      GGGGG rrrrrrrrrrrrrr
					    .gGrrGGGrrrrrGGGrrrGGGG    g  g     GG   g g  GGGG rrrrrrrrrrrrr
				        .gGGGGrrrGGGrrrrrrGGGrrGGG  G   G  g    GG  g   g   GGGG  rrrrrrrrrr
				      .gGGGGGrrrrGGGrrrrrrrG GGGG    G   G  g  GG  g     g     GGGG    rrrrr
				   .gGGGGGGGrrrrrrGGGrrrrrrGGGG   g   G   G  g GG  g      g       GGGGGGGGGG
			         .gGGGGGGGGrrrrrrrGGGGGGGGGGG     g     G  G  gGG  g        g          GGGGG
			       .gGGGGGGGGG rrrrrrrrr gGGGg        g      G  G gGG  G      g   g  g  g rrrr 
			     .gGGGGGGGGG  rrrrrrrrrrrrrrrr        g       G  G     G       g  g   g   rrrrrr
			   .gGGGGGGGGG   rrrrrrrrrrrrrrrr         g        G G     G       g  g  g   grrrrrr
			  .GGGGGGGGGG    rrrrrrrrrrrrrrrr         g g      G  G    G       g  g  g  g rrrrrr
------------------------------------------------------------------------------------------------------------
''')

questions = [
    {
        'type': 'list',
        'name': 'choices_list',
        'message': 'uhhh...can i help you?',
        'choices': [
            'open project',
            'setup a local machine',
            'Ask for opening hours',
            'Talk to the receptionist'
        ]
    },
]

repositories = [
	{
		'type': 'list',
        'name': 'repository_choice',
        'message': 'uhhh...can i help you?',
        'choices': list_repositories()
	}
]

answers = prompt(questions)

def choices(answers):
	for key, value in answers.items():
		if value == "open project":
			repository_choice = prompt(repositories)
			for key, value in repository_choice.items():
				open_project(value)
		elif value == "setup a local machine":
			install_packages()
	print(greeetings)

choices(answers)
