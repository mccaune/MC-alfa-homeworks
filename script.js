//izveidojam date objektu
const date = new Date();
//console.log(date);

const currentYear = date.getFullYear();
//console.log(currentYear);

//const currentYear = date.setFullYear(2520, 0, 13)
//console.log(currentYear);


const reloadCalendar = () => {

    date.setDate(1);
    //console.log(date);

    const firstDayIndex = date.getDay();
    const monthDays = document.querySelector(".days");
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    //colsole.log(lastDay);
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();
    //console.log(prevLastDay);
    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();
    const nextMonthDays = 7 - lastDayIndex;
    //console.log(nextMonthDays);

    const months = [
        "Janvāris",
        "Februāris",
        "Marts",
        "Aprīlis",
        "Maijs",
        "Jūnijs",
        "Jūlijs",
        "Augusts",
        "Septembris",
        "Oktobris",
        "Novembris",
        "Decembris",
    ];

    let days = "";

    document.querySelector(".date h1").innerHTML = months[date.getMonth()];
    document.querySelector(".currentDate").innerHTML = new Date().toDateString();
    document.querySelector(".openedYear").innerHTML = date.getFullYear();

    for (let x = firstDayIndex - 1; x > 0; x--) {
        days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
    }

    for (let i = 1; i <= lastDay; i++) {
        if (
            i === new Date().getDate() &&
            date.getMonth() === new Date().getMonth() && currentYear === date.getFullYear()
        ) {
            days += `<div class="active">${i}</div>`;
        } else {
            days += `<div>${i}</div>`;
        }
    }


    for (let i = 1; i <= nextMonthDays; i++) {
        days += `<div class="next-date">${i}</div>`;
        monthDays.innerHTML = days;
    }



};

let years = "";
let months1 = "";
const selectYears = document.querySelector(".selectYear");
const selectMonths = document.querySelector(".selectMonth");
const months22 = [
    "Janvāris",
    "Februāris",
    "Marts",
    "Aprīlis",
    "Maijs",
    "Jūnijs",
    "Jūlijs",
    "Augusts",
    "Septembris",
    "Oktobris",
    "Novembris",
    "Decembris",
];

function generateYears() {
    for (let i = 1900; i <= 2100; i++) {
        years += `<option value="year">${i}</option>`;
        selectYears.innerHTML = years;
    }
}


function generateMonths() {
    for (let i = 0; i <= months22.length - 1; i++) {
        //months1 += "<option>" + months22[i] + "</option>";
        months1 += `<option>${months22[i]}</option>`
        selectMonths.innerHTML = months1;
    }
}

function submitTest() {
    var x = document.querySelector(".selectYear").options.length;
    let y = document.querySelector(".selectMonth").options.length;
    //console.log(x);
    //console.log(y);

    function getSelectedYear() {

        var optYear;
        for (var i = 0, len = document.querySelector(".selectYear").options.length; i < len; i++) {
            optYear = document.querySelector(".selectYear").options[i];
            if (optYear.selected === true) {
                break;
            }
        }
        return optYear;
    }

    function getSelectedMonth() {

        var optMonth;
        for (var i = 0, len = document.querySelector(".selectMonth").options.length; i < len; i++) {
            optMonth = document.querySelector(".selectMonth").options[i];
            //console.log(optMonth.index);
            if (optMonth.selected === true) {
                break;
            }
        }
        return optMonth.index;
    }



    var optYear = getSelectedYear(x);
    var optMonth = getSelectedMonth(x);

    year = Number(optYear.text);
    month = Number(optMonth);

    date.setFullYear(year, month, 1);
}

function randomYear() {
    let yearR = Math.floor((Math.random() * 10000) + 1);
    let monthR = Math.floor((Math.random() * 11) + 1);
    date.setFullYear(yearR, monthR, 1);
    reloadCalendar();
}

document.querySelector(".submit").addEventListener("click", () => {
    submitTest();
    reloadCalendar();
});

document.querySelector(".selectYear").addEventListener("click", generateYears());
document.querySelector(".selectMonth").addEventListener("click", generateMonths());



document.querySelector(".prev").addEventListener("click", () => {
    date.setMonth(date.getMonth() - 1);
    reloadCalendar();
});

document.querySelector(".next").addEventListener("click", () => {
    date.setMonth(date.getMonth() + 1);
    reloadCalendar();
});

reloadCalendar();