hg = typeof hg =='undefined'? {} : hg;

hg.dt = {};

hg.dt.toTimestamp = function (date){
    return Date.UTC(date.getUTCFullYear(), date.getUTCMonth(),
                    date.getUTCDate(), date.getUTCHours(),
                    date.getUTCMinutes(), date.getUTCSeconds())/1000; //ms to sec
};

hg.dt.now = function(){return new Date();};

hg.dt.today = function(){
    return hg.dt.startOfDay(hg.dt.now());
};


hg.dt.add_days= function(date,days){
    var newDate = new Date(date.getUTCFullYear(), date.getUTCMonth(), date.getUTCDay());
    newDate.setDate(date.getDate() + days);
    return newDate;
};

hg.dt.tommorow = function(){
    return hg.dt.add_days(hg.dt.today(),1);
};

hg.dt.parse = function(str){
    parts=str.split("-");
    return new Date(parseInt(parts[2]),
                    parseInt(parts[0])-1,
                    parseInt(parts[1]));
};

hg.dt.toDateString = function(utc_timestamp){
    var date = hg.dt.fromTimestamp(utc_timestamp);
    return (date.getMonth() + 1) + "-" + date.getDay() + "-" + date.getFullYear();
};

hg.dt.fromTimestamp = function (utc_timestamp){
    var date = new Date(0);
    date.setUTCSeconds(utc_timestamp);
    return $.extend(date,{
        'toTimeString':  function(){
            return (this.getHours() % 12) + ":" + this.getMinutes() +
                ((this.getHours() > 12)?  " PM" : " AM");
        }
    });
};

hg.dt.startOfDay = function(date){
  return new Date(date.getFullYear(), date.getMonth(), date.getDate(), 0, 0, 0);
};

hg.dt.endOfDay = function (date) {
    return new Date(date.getFullYear(), date.getMonth(), date.getDate(), 23, 59, 59);
};

