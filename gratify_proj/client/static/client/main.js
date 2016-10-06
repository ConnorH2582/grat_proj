$(document).ready(function() {
    var activeUserID = $('#active_user_id').attr('value');
    console.log(activeUserID)
    $('#calendar').fullCalendar({
        //hardcoded event to test
        events: [
	        {
	        	title: 'My Event',
	            start: '2016-10-06',
	            description: 'This is a cool event'
	        }
        ],
        // {
        //     url: 'http://myApp.com:8000/app/' + activeUserID + '/calendar/show/',
        //     type: 'GET',
        //     // data: {
        //     //     custom_param1: 'something',
        //     //     custom_param2: 'somethingelse'
        //     // },
        //     error: function() {
        //         alert(
        //             'there was an error while fetching events!'
        //         );
        //     },
            
        //     color: 'yellow', // a non-ajax option
        //     textColor: 'black' // a non-ajax option
        // },
         eventRender: function(event, element) {
        	element.qtip({
            	content: event.title
        });
    },
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,listYear'
        },

        // displayEventTime: false, // don't show the time column in list view
        // THIS KEY WON'T WORK IN PRODUCTION!!!
        // To make your own Google API key, follow the directions here:
        // http://fullcalendar.io/docs/google_calendar/
        // googleCalendarApiKey: 'AIzaSyCEsgOWV_XCH_UF8PGO0AeltrRX6Q-n43A',
        // US Holidays
        // events: 'lkvrj9f8e1npnl5mko1t2oifnc@group.calendar.google.com',
        eventClick: function(event) {
            // opens events in a popup window
            window.open(event.url, 'gcalevent',
                'width=700,height=600');
            return false;
        },
        loading: function(bool) {
            $('#loading').toggle(bool);
        }
    });
});
// $(document).ready(function() {
//     $('#calendar').fullCalendar({
//         googleCalendarApiKey: 'AIzaSyCEsgOWV_XCH_UF8PGO0AeltrRX6Q-n43A',
//         events: {
//             googleCalendarId: 'lkvrj9f8e1npnl5mko1t2oifnc@group.calendar.google.com',
//         	className: 'gcal-event' // an option!

//         }
//     });
// });

// $(document).ready(function() {
//     $('#calendar').fullCalendar({
//         // googleCalendarApiKey: 'AIzaSyCEsgOWV_XCH_UF8PGO0AeltrRX6Q-n43A',
//         events [
            
//         ]
//     });
// });
