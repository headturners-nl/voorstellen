(function(){
  var EMAIL='info@headturners.nl';
  var BASE=(window.HT&&HT.base)||'';
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* current page in menu */
  (function(){var here=location.pathname.replace(/index\.html$/,'').replace(/\/$/,'');
    document.querySelectorAll('header.site .menu a:not(.btn), .dd-panel a').forEach(function(a){
      var p=a.pathname.replace(/index\.html$/,'').replace(/\/$/,'');
      if(p===here&&!a.hash)a.setAttribute('aria-current','page');});
    if(document.querySelector('.dd-panel a[aria-current]'))document.querySelector('.dd > button').setAttribute('aria-current','page');
  })();

  /* menu */
  var burger=document.querySelector('.burger'),menu=document.querySelector('.menu');
  if(burger){burger.addEventListener('click',function(){var o=menu.classList.toggle('open');burger.setAttribute('aria-expanded',String(o));});}
  document.querySelectorAll('.dd').forEach(function(dd){
    var b=dd.querySelector('button');
    b.addEventListener('click',function(e){e.stopPropagation();var o=dd.classList.toggle('open');b.setAttribute('aria-expanded',String(o));});
  });
  document.addEventListener('click',function(){document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open');d.querySelector('button').setAttribute('aria-expanded','false');});});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.dd.open').forEach(function(d){d.classList.remove('open');});}});

  /* before/after */
  function wire(ba){
    var r=ba.querySelector('input'),drag=false;
    function set(v){v=Math.max(0,Math.min(100,+v));ba.style.setProperty('--pos',v+'%');r.value=v;}
    function from(e){var b=ba.getBoundingClientRect();set((e.clientX-b.left)/b.width*100);}
    ba.addEventListener('pointerdown',function(e){drag=true;try{ba.setPointerCapture(e.pointerId)}catch(_){}from(e);r.focus({preventScroll:true});});
    ba.addEventListener('pointermove',function(e){if(drag)from(e);});
    ['pointerup','pointercancel','lostpointercapture'].forEach(function(t){ba.addEventListener(t,function(){drag=false;});});
    r.addEventListener('input',function(){set(r.value)});
    set(50);return set;
  }
  function hint(set){
    if(reduce)return;var t0=null;
    (function step(ts){if(!t0)t0=ts;var k=Math.min(1,(ts-t0)/1800);set((50+Math.sin(k*Math.PI*2)*22*(1-k)).toFixed(1));if(k<1)requestAnimationFrame(step);})(performance.now());
  }
  function watchHint(ba,set){
    if(!('IntersectionObserver' in window))return;
    var io=new IntersectionObserver(function(en){if(en[0].isIntersecting){io.disconnect();setTimeout(function(){hint(set)},300);}},{threshold:.6});
    io.observe(ba);
  }
  function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  var GRIP='<span class="grip" aria-hidden="true"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1F2A44" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 6l-6 6 6 6M15 6l6 6-6 6"/></svg></span>';
  function caseEl(k,i){
    var el=document.createElement('article');el.className='case'+(i%2?' flip':'');
    var tags=(k.diensten||[]).map(function(t){return '<span>'+esc(t)+'</span>'}).join('');
    el.innerHTML='<div class="case-media"><div class="ba">'+
      '<img src="'+esc(BASE+k.voor)+'" alt="Oude website van '+esc(k.naam)+'" loading="lazy" width="1600" height="1000">'+
      '<img class="after" src="'+esc(BASE+k.na)+'" alt="Nieuwe website van '+esc(k.naam)+'" loading="lazy" width="1600" height="1000">'+
      '<span class="lay lay-l" aria-hidden="true"><span class="chip l">Voor</span></span><span class="lay lay-r" aria-hidden="true"><span class="chip r">Na</span></span><span class="bar" aria-hidden="true"></span>'+
      '<input type="range" min="0" max="100" value="50" aria-label="Vergelijk de oude en nieuwe website van '+esc(k.naam)+'">'+GRIP+'</div></div>'+
      '<div class="case-text"><p class="case-where">'+esc(k.branche)+' in '+esc(k.plaats)+'</p><h3>'+esc(k.naam)+'</h3><p>'+esc(k.resultaat)+'</p>'+
      (tags?'<div class="case-tags">'+tags+'</div>':'')+
      '<a class="link" href="'+esc(k.url)+'" target="_blank" rel="noopener">Bekijk de site van '+esc(k.naam)+'</a></div>';
    var ba=el.querySelector('.ba');el._set=wire(ba);el._ba=ba;return el;
  }
  document.querySelectorAll('[data-cases]').forEach(function(box){
    var limit=+box.getAttribute('data-cases')||99;
    fetch(BASE+'klanten.json',{cache:'no-store'}).then(function(r){return r.json()}).then(function(list){
      list.slice(0,limit).forEach(function(k,i){var el=caseEl(k,i);box.appendChild(el);if(i===0)watchHint(el._ba,el._set);});
    }).catch(function(){box.innerHTML='<p>De voorbeelden konden niet laden. Ververs de pagina om het opnieuw te proberen.</p>'});
  });

  /* price switch */
  document.querySelectorAll('.switch').forEach(function(sw){
    var scope=sw.closest('section')||document,btns=sw.querySelectorAll('button');
    btns.forEach(function(b){b.addEventListener('click',function(){
      var m=b.getAttribute('data-mode');
      btns.forEach(function(x){x.setAttribute('aria-pressed',String(x===b))});
      scope.querySelectorAll('[data-huren]').forEach(function(n){n.textContent=n.getAttribute('data-'+m)});
      scope.querySelectorAll('.only-huren').forEach(function(n){n.hidden=(m!=='huren')});
    })});
  });

  /* contact form */
  var f=document.getElementById('aanvraag');
  if(f){
    var params=new URLSearchParams(location.search),pre=params.get('dienst');
    if(pre){f.querySelectorAll('input[name=dienst]').forEach(function(c){if(c.value===pre)c.checked=true;});}
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var msg=document.getElementById('form-msg'),naam=f.naam.value.trim(),mail=f.email?f.email.value.trim():'';
      msg.className='form-msg';
      if(!naam){msg.textContent='Vul je naam in, dan weet ik voor wie het is.';msg.className='form-msg err';f.naam.focus();return}
      if(f.email&&!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(mail)){msg.textContent='Vul je mailadres in, dan kan ik je voorstel sturen.';msg.className='form-msg err';f.email.focus();return}
      var dienst=[].map.call(f.querySelectorAll('input[name=dienst]:checked'),function(c){return c.value}).join(', ')||'Gratis voorstel website';
      var data={naam:naam,email:mail,bedrijf:f.bedrijf.value.trim(),telefoon:f.telefoon.value.trim(),site:f.site.value.trim(),dienst:dienst,bericht:f.bericht.value.trim(),website_url:f.website_url?f.website_url.value:''};
      if(window.HT&&HT.api){
        var btn=f.querySelector('button[type=submit]');btn.disabled=true;msg.textContent='Even geduld, je aanvraag wordt verstuurd.';
        fetch(HT.api,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)})
          .then(function(r){return r.json().then(function(j){return {ok:r.ok,j:j}})})
          .then(function(res){
            btn.disabled=false;
            if(res.ok&&res.j&&res.j.ok){f.reset();msg.className='form-msg ok';msg.textContent='Dank je wel. Je aanvraag is binnen en ik neem binnen twee werkdagen contact met je op.';}
            else{msg.className='form-msg err';msg.textContent=(res.j&&res.j.message)||'Versturen lukte niet. Mail je aanvraag naar '+EMAIL+'.';}
          })
          .catch(function(){btn.disabled=false;msg.className='form-msg err';msg.textContent='Versturen lukte niet. Mail je aanvraag naar '+EMAIL+'.';});
        return;
      }
      var body='Naam: '+naam+'\nMail: '+mail+'\nBedrijf: '+data.bedrijf+'\nTelefoon: '+data.telefoon+'\nHuidige website of Instagram: '+data.site+'\nInteresse: '+dienst+'\n\n'+data.bericht;
      location.href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Aanvraag van '+(data.bedrijf||naam))+'&body='+encodeURIComponent(body);
      msg.textContent='Je mailprogramma is geopend met je gegevens erin. Druk daar op verzenden.';
    });
  }
  var y=document.getElementById('jaar');if(y)y.textContent=new Date().getFullYear();
})();
