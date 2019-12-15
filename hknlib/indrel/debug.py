from .settings import DEBUG

def generate_test_email():
    text = "Dear Pauline,\n\n"
    text += "My name is Eric Wang and I represent UC Berkeley's Electrical Engineering and Computer Science Honor Society, Eta Kappa Nu (HKN). "
    text += "I am reaching out to you because HKN would like to partner with Wish this upcoming Spring semester to help you connect with our student body "
    text += "for any internship or full-time job opportunities you may have available. I noticed that you have an event scheduled with the EECS department "
    text += "for the coming semester, but do not yet have a student group to help with logistics. HKN would love to help with the logistics for your event!\n\n"
    text += "UC Berkeley’s EECS curriculum and department is one of the most highly ranked and competitive programs in the country, and HKN members belong to "
    text += "the top quarter of the Junior and top third of the Senior undergraduate class. In the past two years, we've hosted over 60 events with an average "
    text += "attendance of over 50 students each.\n\nIf you are interested in partnering with us for other events at UC Berkeley, we could organize larger events "
    text += "like tech talks, or more personal one-on-one coffee chats or dinner events. You can read about the recruiting events that have worked well in the past here.\n\n"
    text += "These are just a few of the options, and I’d love to jump on a call and learn more about what kind of event you’re looking to host to see how we can best help you.\n\n"
    text += "Also, HKN organizes outreach events for local high school and middle school students to pursue their interests in electrical engineering and computer science. "
    text += "If you are interested in sponsoring or donating equipment for these events, we’d love to connect you with our Service event team.\n\n"
    text += "If you have any questions or concerns, please do not hesitate to contact me. We look forward to hearing from you!\n\n"
    text += "Best,\nEric Wang\nIndustrial Relations\nEta Kappa Nu, Mu Chapter\nUC Berkeley"
    print(text)
    return text