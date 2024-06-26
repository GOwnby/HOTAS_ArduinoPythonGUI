const messages={'en':{'copy':'Copy','copy_to_clipboard':'Copy to clipboard','copy_success':'Copied!','copy_failure':'Failed to copy',},'es':{'copy':'Copiar','copy_to_clipboard':'Copiar al portapapeles','copy_success':'¡Copiado!','copy_failure':'Error al copiar',},'de':{'copy':'Kopieren','copy_to_clipboard':'In die Zwischenablage kopieren','copy_success':'Kopiert!','copy_failure':'Fehler beim Kopieren',},'fr':{'copy':'Copier','copy_to_clipboard':'Copier dans le presse-papier','copy_success':'Copié !','copy_failure':'Échec de la copie',},'ru':{'copy':'Скопировать','copy_to_clipboard':'Скопировать в буфер','copy_success':'Скопировано!','copy_failure':'Не удалось скопировать',},'zh-CN':{'copy':'复制','copy_to_clipboard':'复制到剪贴板','copy_success':'复制成功!','copy_failure':'复制失败',},'it':{'copy':'Copiare','copy_to_clipboard':'Copiato negli appunti','copy_success':'Copiato!','copy_failure':'Errore durante la copia',}}
let locale='en'
if(document.documentElement.lang!==undefined&&messages[document.documentElement.lang]!==undefined){locale=document.documentElement.lang}
let doc_url_root=DOCUMENTATION_OPTIONS.URL_ROOT;if(doc_url_root=='#'){doc_url_root='';}
let iconCheck=`<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-check" width="44" height="44" viewBox="0 0 24 24" stroke-width="2" stroke="#22863a" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <title>${messages[locale]['copy_success']}</title>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <path d="M5 12l5 5l10 -10" />
</svg>`
let iconCopy=``;if(!iconCopy){iconCopy=`<svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-copy" width="44" height="44" viewBox="0 0 24 24" stroke-width="1.5" stroke="#000000" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <title>${messages[locale]['copy_to_clipboard']}</title>
  <path stroke="none" d="M0 0h24v24H0z" fill="none"/>
  <rect x="8" y="8" width="12" height="12" rx="2" />
  <path d="M16 8v-2a2 2 0 0 0 -2 -2h-8a2 2 0 0 0 -2 2v8a2 2 0 0 0 2 2h2" />
</svg>`}
const runWhenDOMLoaded=cb=>{if(document.readyState!='loading'){cb()}else if(document.addEventListener){document.addEventListener('DOMContentLoaded',cb)}else{document.attachEvent('onreadystatechange',function(){if(document.readyState=='complete')cb()})}}
const codeCellId=index=>`codecell${index}`
const clearSelection=()=>{if(window.getSelection){window.getSelection().removeAllRanges()}else if(document.selection){document.selection.empty()}}
var timeoutIcon=2000;var timeoutSuccessClass=1500;const temporarilyChangeTooltip=(el,oldText,newText)=>{el.setAttribute('data-tooltip',newText)
el.classList.add('success')
setTimeout(()=>el.classList.remove('success'),timeoutSuccessClass)
setTimeout(()=>el.setAttribute('data-tooltip',oldText),timeoutIcon)}
const temporarilyChangeIcon=(el)=>{el.innerHTML=iconCheck;setTimeout(()=>{el.innerHTML=iconCopy},timeoutIcon)}
const addCopyButtonToCodeCells=()=>{if(window.ClipboardJS===undefined){setTimeout(addCopyButtonToCodeCells,250)
return}
const COPYBUTTON_SELECTOR='div.highlight pre';const codeCells=document.querySelectorAll(COPYBUTTON_SELECTOR)
codeCells.forEach((codeCell,index)=>{const id=codeCellId(index)
codeCell.setAttribute('id',id)
const clipboardButton=id=>`<button class="copybtn o-tooltip--left" data-tooltip="${messages[locale]['copy']}" data-clipboard-target="#${id}">
      ${iconCopy}
    </button>`
codeCell.insertAdjacentHTML('afterend',clipboardButton(id))})
function escapeRegExp(string){return string.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
function filterText(target,exclude){const clone=target.cloneNode(true);if(exclude){clone.querySelectorAll(exclude).forEach(node=>node.remove());}
return clone.innerText;}
function formatCopyText(textContent,copybuttonPromptText,isRegexp=false,onlyCopyPromptLines=true,removePrompts=true,copyEmptyLines=true,lineContinuationChar="",hereDocDelim=""){var regexp;var match;var useLineCont=!!lineContinuationChar
var useHereDoc=!!hereDocDelim
if(isRegexp){regexp=new RegExp('^('+copybuttonPromptText+')(.*)')}else{regexp=new RegExp('^('+escapeRegExp(copybuttonPromptText)+')(.*)')}
const outputLines=[];var promptFound=false;var gotLineCont=false;var gotHereDoc=false;const lineGotPrompt=[];for(const line of textContent.split('\n')){match=line.match(regexp)
if(match||gotLineCont||gotHereDoc){promptFound=regexp.test(line)
lineGotPrompt.push(promptFound)
if(removePrompts&&promptFound){outputLines.push(match[2])}else{outputLines.push(line)}
gotLineCont=line.endsWith(lineContinuationChar)&useLineCont
if(line.includes(hereDocDelim)&useHereDoc)
gotHereDoc=!gotHereDoc}else if(!onlyCopyPromptLines){outputLines.push(line)}else if(copyEmptyLines&&line.trim()===''){outputLines.push(line)}}
if(lineGotPrompt.some(v=>v===true)){textContent=outputLines.join('\n');}
if(textContent.endsWith("\n")){textContent=textContent.slice(0,-1)}
return textContent}
var copyTargetText=(trigger)=>{var target=document.querySelector(trigger.attributes['data-clipboard-target'].value);let exclude='.linenos';let text=filterText(target,exclude);return formatCopyText(text,'>>> |\\.\\.\\. ',true,true,true,true,'','')}
const clipboard=new ClipboardJS('.copybtn',{text:copyTargetText})
clipboard.on('success',event=>{clearSelection()
temporarilyChangeTooltip(event.trigger,messages[locale]['copy'],messages[locale]['copy_success'])
temporarilyChangeIcon(event.trigger)})
clipboard.on('error',event=>{temporarilyChangeTooltip(event.trigger,messages[locale]['copy'],messages[locale]['copy_failure'])})}
runWhenDOMLoaded(addCopyButtonToCodeCells)