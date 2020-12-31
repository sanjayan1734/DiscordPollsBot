file = open('eventplanner.txt',"a")

class event_planner():
    event_id = '0'
    event_name = 'test_event'
    event_time = '28/12/2020 19:00'
    event_status = 'pending'

    def add_event(self):
        file.write('{} \n{} \n{} \n{} \n'.format(event_planner.event_id,event_planner.event_name,event_planner.event_time,event_planner.event_status))
   

e = event_planner()
e.add_event()
file.close()