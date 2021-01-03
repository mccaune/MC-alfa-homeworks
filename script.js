//izveidojam date objektu
const date = new Date();
//console.log(date); //konsolē redzam tekošās dienas datumu

const currentYear = date.getFullYear();

//console.log(currentYear);

//const currentYear = date.setFullYear(2520, 0, 13)
//console.log(currentYear);


const reloadCalendar = () => {
    //const currentYear = date.getFullYear();


    //iegūstam pilnu datumu mēneša pirmajai dienai.- "Date Tue Dec 01 2020"
    date.setDate(1);
    //console.log(date);

    //nedēļas dienas atbilst array vērībām (P;O;O;T;C;P;Se;Sv) [0-6]
    const firstDayIndex = date.getDay();
    //console.log(firstDayIndex) //iegūstam vērtību 2, jo 1.decembris ir otrdienā

    //iezīmē .days klases elementu, ko vēlāk izmantos lai papildinātu ar reālajām mēneša dienām
    const monthDays = document.querySelector(".days");

    //lastDay - iegūst tekošā mēneša garumu dienās
    const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
    //colsole.log(lastDay); //konsolē redzam tekošā mēneša pēdējo datumu un kas tā par dienu

    //iegūst iepriekšējā mēneša pēdējās dienas vērtību. Svarīgi, lai saprastu kāda vertībai
    const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();
    //console.log(prevLastDay); //iegūstam vērtību 30, jo novembrī pēdējais datums bija 30

    const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();

    const nextMonthDays = 7 - lastDayIndex;
    //console.log(nextMonthDays);


    // Array ar visiem iespējamajiem mēnešiem, idexi no 0 līdz 11
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

    //definē tikšu days array. tajā vēlāk pievieno visus kalendāra datumus un nosūta uz HTML
    let days = "";

    //iezīmējam <h1></h1>, kas atrodas zem klases .date; tam piešķiram tekošā mēneša vērtību no months array izvēloties to, kas atbilst selektējot ar date.getMonth() metodi
    document.querySelector(".date h1").innerHTML = months[date.getMonth()];
    //iezīmējam <p>, kas atrodas zem klases .date; tam piešķiram tekošā datuma vērtību, kas datumam kuru iegūst ar .toDateString metodi
    document.querySelector(".currentDate").innerHTML = new Date().toDateString();

    document.querySelector(".openedYear").innerHTML = date.getFullYear();

    //FirstDayIndex ir 2, jo 1. decembris ir otrdiena. For cikla iterācija notiks 1 reizi, un kalendārā tiks pievienots viens datums no iepriekšējā mēneša, kas atradīsies pirmdienā. Tiek izveidots <div> elements ar papildus klasi - "prev-date"
    for (let x = firstDayIndex - 1; x > 0; x--) {
        days += `<div class="prev-date">${prevLastDay - x + 1}</div>`;
    }

    //For cikls attēlo visas tekošās mēneša dienas (svarīgs ir skaits 30 vai 31) LastDay mainīgais glabā esošā mēneša dienu skaitu (28;30;31) iterācija attiecīgi arī notiek tik reižu, cik mēnesī dienu un tik dienas pievieno kalendārā. Tiek izveidots <div> elements bez papildus klases.
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


    // get selected option in sel (reference obtained above)
    var optYear = getSelectedYear(x);
    var optMonth = getSelectedMonth(x);

    year = Number(optYear.text);
    month = Number(optMonth);

    date.setFullYear(year, month, 1);
    // display its value and text
    //console.log(opt.value);
    //console.log(opt.text);
}

function randomYear() {
    let yearR = Math.floor((Math.random() * 10000) + 1);
    let monthR = Math.floor((Math.random() * 11) + 1);
    date.setFullYear(yearR, monthR, 1);
    reloadCalendar();
}

document.querySelector(".submit").addEventListener("click", () => {
    submitTest();
    //year = Number(opt.text);
    //date.setFullYear(year, 0, 13);
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