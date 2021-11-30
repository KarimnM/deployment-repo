
function getCssValuePrefix()
{
    var rtrnVal = '';//default to standard syntax
    var prefixes = ['-o-', '-ms-', '-moz-', '-webkit-'];
    // Create a temporary DOM object for testing
    var dom = document.createElement('div');
    for (var i = 0; i < prefixes.length; i++)
    {
        // Attempt to set the style
        dom.style.background = prefixes[i] + 'linear-gradient(#000000, #ffffff)';
        // Detect if the style was successfully set
        if (dom.style.background)
        {
            rtrnVal = prefixes[i];
        }
    }
    dom = null;
    delete dom;
    return rtrnVal;
}

function hexToRgb(hex)
{
    var result = /^#?([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})([a-f\d]{2})?$/i.exec(hex);
    return result ? {
        r: parseInt(result[1], 16),
        g: parseInt(result[2], 16),
        b: parseInt(result[3], 16)
    } : null;
}


const hoursPerCell = 2;
const calendarStartHour = 8;
const calendarStartMinutes = calendarStartHour * 60;
const daysInCalendarWeek = 5;
function getCellIndexForTime(startDayNumber, startHour, startMinute)
{
    console.assert(0 <= startDayNumber && startDayNumber < 5); // 0 = Monday, 4 = Friday
    console.assert(startHour >= calendarStartHour);
    console.assert(0 <= startMinute && startMinute < 60);
    var startTime = startHour + startMinute/60;
    return Math.floor((startTime - calendarStartHour) / hoursPerCell) * daysInCalendarWeek + startDayNumber;
}

function eventStartPercent(startHour, startMinute)
{
    var startTime = startHour + startMinute/60;
    var startPercent = (startTime - calendarStartHour) % hoursPerCell / hoursPerCell * 100;
    return startPercent.toString() + "%";
}

function eventHeightPercent(eventDurationHours)
{
    var heightPercent = eventDurationHours / hoursPerCell * 100;
    return heightPercent.toString() + "%";
}

function addTimeToCalendar(startDayNumber, startHour, startMinute, endHour, endMinute, color1, color2=null)
{
    if(color2 == null)
        color2 = color1;
    // example run:    addTimeToCalendar(1, 13, 30, 0, 0, 'red');
    var tableCells = document.getElementsByClassName("content")[0];
    console.log(tableCells);

    var index = getCellIndexForTime(startDayNumber, startHour, startMinute);
    var targetDiv = tableCells.children[Math.floor(index)];

    var startPercent = eventStartPercent(startHour, startMinute);
    var eventDuration = endHour - startHour + (endMinute - startMinute) / 60;
    var heightPercent = eventHeightPercent(eventDuration);

    var eventDiv = document.createElement("div");
    eventDiv.setAttribute("class", "eventDiv");

    eventDiv.style.position = 'absolute';

    eventDiv.style.display = 'block';
    eventDiv.style.top = startPercent;
    eventDiv.style.left = '0px';
    eventDiv.style.boxSizing = "border-box";
    eventDiv.style.background = getCssValuePrefix() + "linear-gradient(135deg, " + color1 + ", " + color2 + ")";
    eventDiv.style.height = heightPercent;
    eventDiv.style.width = '100%';


    var rgb = hexToRgb(color1);
    var boxShadowString = "0 20px 30px 0 rgba(" + rgb.r + ", " + rgb.g + ", " + rgb.b + ", 0.3)";
    console.log(rgb);
    console.log(boxShadowString);
    eventDiv.addEventListener('mouseenter', function() {
         // $(this).css("box-shadow", "5px 5px 5px #555");
         eventDiv.style.transform = "scale(1.05)";
         eventDiv.style.boxShadow = boxShadowString;
         /* box-shadow: 0 20px 30px 0 rgba(238, 142, 188, 0.3);   var(--eventDivBoxShadow); */
      });
    eventDiv.addEventListener('mouseleave', function(){
        eventDiv.style.transform = "scale(1.00)";
        eventDiv.style.boxShadow = "none";
    });


    targetDiv.appendChild(eventDiv);

}

