(function(){
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hdr=document.querySelector('header.site');
  function hh(){if(hdr)document.documentElement.style.setProperty('--hh',hdr.offsetHeight+'px');}
  hh();addEventListener('resize',hh);

  /* reveal on scroll */
  var rv=document.querySelectorAll('.reveal');
  if(reduce||!('IntersectionObserver' in window)){rv.forEach(function(e){e.classList.add('in')});}
  else{var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('in');io.unobserve(x.target);}})},{threshold:.15});rv.forEach(function(e){io.observe(e)});}

  /* rail */
  var steps=['kijken','kiezen','voelen','schrappen','live'],links={};
  document.querySelectorAll('.rail a').forEach(function(a){links[a.dataset.step]=a;});
  if('IntersectionObserver' in window){
    var ro=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){var cur=x.target.dataset.ch,i=steps.indexOf(cur);
      steps.forEach(function(s,j){links[s].classList.toggle('on',j===i);links[s].classList.toggle('done',j<i);});}})},{rootMargin:'-45% 0px -50% 0px'});
    document.querySelectorAll('[data-ch]').forEach(function(s){ro.observe(s)});
  }

  /* 1 pins */
  var pins=[].slice.call(document.querySelectorAll('.pin'));
  pins.forEach(function(p){
    p.addEventListener('click',function(e){
      e.stopPropagation();
      var pop=p.nextElementSibling,open=p.getAttribute('aria-expanded')!=='true';
      pins.forEach(function(q){q.setAttribute('aria-expanded','false');q.nextElementSibling.classList.remove('open');});
      if(open){p.setAttribute('aria-expanded','true');pop.classList.add('open');p.classList.add('seen');}
    });
  });
  document.addEventListener('click',function(){pins.forEach(function(q){q.setAttribute('aria-expanded','false');q.nextElementSibling.classList.remove('open');});});

  /* 2 words */
  var wbox=document.querySelector('.words');
  if(wbox){
    var btns=[].slice.call(wbox.querySelectorAll('button')),cnt=document.querySelector('.words-count'),res=document.querySelector('.words-result'),picked=res.querySelector('.picked');
    var label=['Nog drie te gaan','Nog twee','Nog eentje'];
    btns.forEach(function(b){b.setAttribute('aria-pressed','false');b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')==='true';b.setAttribute('aria-pressed',String(!on));update();});});
    function update(){
      var sel=btns.filter(function(b){return b.getAttribute('aria-pressed')==='true'});
      var full=sel.length>=3;
      btns.forEach(function(b){b.disabled=full&&b.getAttribute('aria-pressed')!=='true';});
      cnt.textContent=full?'':label[sel.length];
      if(full){picked.textContent=sel.map(function(b){return b.textContent.toLowerCase()}).join(', ');res.hidden=false;}
      else res.hidden=true;
    }
    res.querySelector('.again').addEventListener('click',function(){btns.forEach(function(b){b.setAttribute('aria-pressed','false')});update();btns[0].focus();});
  }

  /* 3 dial */
  var mock=document.getElementById('mock'),dial=document.getElementById('dial'),note=document.querySelector('.dial-note'),pal=document.querySelector('.pal');
  function ss(a,b,t){t=Math.max(0,Math.min(1,(t-a)/(b-a)));return t*t*(3-2*t);}
  function mix(c1,c2,k){var a=c1.match(/\w\w/g).map(function(h){return parseInt(h,16)}),b=c2.match(/\w\w/g).map(function(h){return parseInt(h,16)});return 'rgb('+a.map(function(v,i){return Math.round(v+(b[i]-v)*k)}).join(',')+')';}
  var notes=[[0,'Koel, wit en algemeen.'],[.2,'Eerst de kleur. Warm hout in plaats van wit.'],[.5,'Dan de letter. Rustig, met karakter.'],[.75,'En dan bellen, appen en een afspraak altijd in beeld.'],[.97,'Dit is Samia.']];
  function setT(t){
    var k1=ss(.15,.36,t),k2=ss(.45,.65,t),k3=ss(.72,.9,t);
    mock.style.setProperty('--k1',k1.toFixed(3));mock.style.setProperty('--k2',k2.toFixed(3));mock.style.setProperty('--k3',k3.toFixed(3));
    mock.style.setProperty('--hb',mix('ffffff','E9E2DC',k1));
    var n=notes[0][1];notes.forEach(function(x){if(t>=x[0])n=x[1]});if(note.textContent!==n)note.textContent=n;
    pal.classList.toggle('on',t>.3);
  }
  if(mock&&dial){
    dial.addEventListener('input',function(){touched=true;setT(dial.value/100)});var touched=false;
    setT(0);
    /* a small nudge the first time it comes into view, so you see it moves */
    if(!reduce&&'IntersectionObserver' in window){
      dial.addEventListener('pointerdown',function(){touched=true});
      var mo=new IntersectionObserver(function(en){if(en[0].isIntersecting){mo.disconnect();setTimeout(function(){
        if(touched)return;var t0=null;(function step(ts){if(touched)return;if(!t0)t0=ts;var k=Math.min(1,(ts-t0)/1600);var v=Math.sin(k*Math.PI)*.3;dial.value=v*100;setT(v);if(k<1)requestAnimationFrame(step);})(performance.now());
      },500);}},{threshold:.6});
      mo.observe(mock);
    }
  }

  /* 4 cut */
  var cut=document.querySelector('.cut'),old=document.getElementById('cutOld'),nw=document.getElementById('cutNew'),cb=document.getElementById('cutBtn');
  if(cut){
    var src=old.textContent;
    function wrap(){old.innerHTML=src.split(' ').map(function(w){return '<span class="w">'+w+'</span>'}).join(' ');}
    wrap();
    var target='Ik ben Samia, en ik neem de tijd voor jou.',busy=false;
    cb.addEventListener('click',function(){
      if(busy)return;
      if(cut.classList.contains('done')){cut.classList.remove('done');nw.textContent='';nw.classList.remove('end');wrap();cb.textContent='Schrap wat niet nodig is';return;}
      busy=true;var ws=[].slice.call(old.querySelectorAll('.w'));
      var order=ws.map(function(_,i){return i}).sort(function(){return Math.random()-.5});
      var d=reduce?0:28;
      order.forEach(function(i,j){setTimeout(function(){ws[i].classList.add('x')},j*d);});
      setTimeout(function(){
        cut.classList.add('done');
        var i=0;(function type(){nw.textContent=target.slice(0,i);if(i<target.length){i++;setTimeout(type,reduce?0:45);}else{nw.classList.add('end');busy=false;cb.textContent='Nog een keer';}})();
      },order.length*d+500);
    });
  }

  /* 5 typed url */
  var ty=document.querySelector('.typed');
  if(ty){
    var txt=ty.dataset.text;
    if(reduce||!('IntersectionObserver' in window)){ty.textContent=txt;}
    else{var to=new IntersectionObserver(function(en){if(en[0].isIntersecting){to.disconnect();var i=0;(function t(){ty.textContent=txt.slice(0,i);if(i++<txt.length)setTimeout(t,70);})();}},{threshold:.8});to.observe(ty);}
  }
})();
