// Data
const ecDropdownData = [
  {
    id: 0,
    value: null,
    img: null,
    label: '--- Please Select ---',
    manual: []
  },
  {
    id: 1,
    value: 'outlook-new-win',
    img: '/static/win-ms-outlook-icon.png',
    label: 'Microsoft Outlook (new) for Windows',
    manual: [
      'Open Outlook.',
      'Click on File in the top menu.',
      'Select Options.',
      'In the Mail category, click on Signatures.',
      'Click the New button to create a new signature.',
      'Enter a name for the signature.',
      'In the Edit signature field, paste your new signature from the generator.',
      'Click OK to save the signature.',
      'To use the new signature, compose a new email and select the signature from the Signature dropdown menu.'
    ]
  },
  {
    id: 2,
    value: 'outlook-win',
    img: '/static/win-ms-outlook-icon.png',
    label: 'Microsoft Outlook (old) for Windows',
    manual: [
      'Open Outlook.',
      'Click on File in the top menu.',
      'Select Options.',
      'In the Mail category, click on Signatures.',
      'Click the New button to create a new signature.',
      'Enter a name for the signature.',
      'In the Edit signature field, paste your new signature from the generator.',
      'Click OK to save the signature.',
      'To use the new signature, compose a new email and select the signature from the Signature dropdown menu.'
    ]
  },
  {
    id: 3,
    value: 'outlook-new-mac',
    img: '/static/mac-ms-outlook-icon.png',
    label: 'Microsoft Outlook (new) for MacOS',
    manual: [
      'Select New Email.',
      'Select Signature > Manage Signatures.',
      'Select + and type a name for the signature',
      'Under Signature, paste your new signature from the generator and click save.',
      'Select Signature > Pick your new Signature.'
    ]
  },
  {
    id: 4,
    value: 'outlook-mac',
    img: '/static/mac-ms-outlook-icon.png',
    label: 'Microsoft Outlook (old) for MacOS',
    manual: [
      'Open Outlook.',
      'Go to Outlook in the top menu and select Preferences.',
      'Click on Signatures.',
      'Click the + button to add a new signature.',
      'Enter a name for the signature.',
      'In the Signature field, paste your new signature from the generator.',
      'Close the Signatures window to save the signature.',
      'To use the new signature, go to New Email and select the signature from the Signature dropdown menu.'
    ]
  },
  // { id: 5, value: 'mobile-outlook-ios', img: '/static/ios-ms-outlook-icon.png', label: 'Microsoft Outlook for iOS' },
  {
    id: 6,
    value: 'mobile-outlook-and',
    img: '/static/and-ms-outlook-icon.png',
    label: 'Microsoft Outlook for Android',
    manual: [
      'Create the signature on your desktop Outlook.',
      'Compose a new email with the new signature and send it to yourself.',
      'Open the email in Outlook on your mobile device.',
      'Tap and hold on the signature to copy it.',
      'Go to Outlook settings on your mobile device, navigate to <strong>Signature</strong>, and paste the copied signature.'
    ]
  },
  {
    id: 7,
    value: 'native-win',
    img: '/static/win-native-mail-icon.png',
    label: 'Mail for Windows',
    manual: [
      'Open the Mail app on your Windows device.',
      'Click on the Settings gear icon at the bottom left.',
      'Select Signature.',
      'Toggle the Use an email signature switch to On.',
      'Enter your desired signature in the text field.',
      'Click Save to save your signature.'
    ]
  },
  {
    id: 8,
    value: 'native-mac',
    img: '/static/mac-native-mail-icon.png',
    label: 'Mail for MacOS',
    manual: [
      'Click Download button above and save your signature file.',
      'Open the Mail app on your Mac.',
      'Click on Mail in the top menu and select Settings.',
      'Go to the Signatures tab.',
      'Click the + button to create a new signature.',
      'Enter a name for the signature.',
      'Close the pop-up window and close Mac Mail completely.',
      'Open Finder, Select Go -> Go to Folder, type ~/Library/Mail and press enter',
      'Open folder V10 (or with higher number if exist) and go to MailData > Signatures.',
      'Find the latest file with .mailsignature extension. Copy its name and use it to rename the downloaded file (with extension).',
      'Replace downloaded file with file in Signatures. Right-click on the file, select Get Info > Lock the file and close pop-up.',
      'Open Mail app > Create a new email and select new signature from the dropdown menu.'
    ]
  },
  // { id: 9, value: 'mobile-native-ios', img: '/static/ios-native-mail-icon.png', label: 'Mail for iOS' },
]

// Form validation
function validateForm() {
  let errors = [];
  let errorsEls = document.querySelectorAll('.error');
  errorsEls.forEach((error) => (error.innerHTML = ''));

  let nameEl = document.getElementById('full_name');
  if (nameEl?.value.trim() === '') {
    errors.push({
      target: document.getElementById('full_name-error'),
      msg: 'Please enter your name',
      input: nameEl
    })
  }

  let emailEl = document.getElementById('email');
  if (emailEl && !validateEmail(emailEl.value)) {
    errors.push({
      target: document.getElementById('email-error'),
      msg: 'Please enter a valid email address',
      input: nameEl
    })
  }

  let jobRoleEl = document.getElementById('job_role');
  if (jobRoleEl?.value.trim() === '') {
    errors.push({
      target: document.getElementById('job_role-error'),
      msg: 'Please enter your role',
      input: nameEl
    })
  }

  let emailClientEl = document.getElementById('email-client');
  if (emailClientEl?.value.trim() === 'null') {
    errors.push({
      target: document.getElementById('email-client-error'),
      msg: 'Please select your email client',
      input: emailClientEl
    })
  }

  let phoneEl = document.getElementById('phone');
  if (phoneEl && !validatePhoneNumber(phoneEl.value)) {
    errors.push({
      target: document.getElementById('phone-error'),
      msg: `Phone number (${phoneEl.value} should start with a + followed by 10 to 15 digits without any other characters`,
      input: phoneEl
    })
  }

  let smLinkEls = document.querySelectorAll('.js-sm-link');
  smLinkEls.forEach((linkEl) => {
    if (linkEl.value.length !== 0 && !validateUrl(linkEl.value)) {
      errors.push({
        target: linkEl.parentNode.querySelector('.js-sm-link-error'),
        msg: `Link have to be valid URL.`,
        input: linkEl
      })
    }
  });

  let ctaLinkEls = document.querySelectorAll('.js-cta-link');
  ctaLinkEls.forEach((linkEl) => {
    let ctaDescEl = linkEl.closest('.form-wrapper')?.querySelector('.js-cta-desc');
    if (ctaDescEl?.value.length !== 0 && linkEl.value.length === 0) {
      errors.push({
        target: linkEl.closest('.form-group').querySelector('.js-cta-link-error'),
        msg: `Please enter link URL.`,
        input: linkEl
      })
    } else if (linkEl.value.length !== 0 && !validateUrl(linkEl.value)) {
      errors.push({
        target: linkEl.closest('.form-group').querySelector('.js-cta-link-error'),
        msg: `Link have to be valid URL.`,
        input: linkEl
      })
    }
  });

  let ctaDescEls = document.querySelectorAll('.js-cta-desc');
  ctaDescEls.forEach((descEl) => {
    let ctaLinkEl = descEl.closest('.form-wrapper')?.querySelector('.js-cta-link');
    if (ctaLinkEl?.value.length !== 0 && descEl.value.length === 0) {
      errors.push({
        target: descEl.closest('.form-group').querySelector('.js-cta-desc-error'),
        msg: `Please enter CTA description.`,
        input: descEl
      })
    }
  });

  if (errors.length > 0) {
    errors.forEach(error => {
      if (!error.target) return;
      error.target.innerHTML = error.msg;
    })
    scrollTo(errors[0].target);

    return false;
  }

  return true;
}

function validateEmail(email) {
  const re =
    /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
  return re.test(String(email).toLowerCase());
}

function validatePhoneNumber(phone) {
  const re = /^\+[0-9]{10,15}$|^$/;
  return re.test(String(phone));
}

function validateUrl(url) {
  const re =
    /^((https?:\/\/)|www\.)[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&\/=]*)$/;
  return re.test(String(url));
}

function prefillEmail(full_name) {
  let email = document.getElementById('email');
  if (email && full_name && !email.value) {
    let parts = full_name.split(/[ \t]+/);
    email.value =
      (parts.length > 1
        ? [parts[0], parts.slice(1).join('')].join('.')
        : parts[0]
      ).toLowerCase() + '@xebia.com';
  }
}

// Clone mechanism
function cloneFormGroup(cloneTarget, options = {}) {
  let targetEl = document.querySelector(cloneTarget);

  if (!targetEl) return;

  let cloneEl = targetEl.initialNode.cloneNode(true);
  let cloneCount = parseInt(targetEl.dataset.cloneCount ?? 0) + 1;

  if (!!options.remove && Array.isArray(options.remove)) {
    options.remove.forEach((selector) =>
      cloneEl.querySelector(selector)?.remove()
    );
  }

  cloneEl.classList.remove(cloneTarget.replace(/^\./, ''));
  cloneEl.classList.add('form-clone');
  cloneEl.removeAttribute('data-clone-count');

  targetEl.dataset.cloneCount = cloneCount;
  cloneEl = prepareCloneFields(cloneCount, cloneEl);

  targetEl?.parentNode.appendChild(cloneEl);

  let removeBtn = cloneEl.querySelector('.js-form-clone-remove');
  if (removeBtn) {
    cloneRemoveBtnInit(removeBtn);
  }

  allMaxCharsCounterInit();
  allSelectInit();
  onSmSelectChangeInit();

  return cloneEl;
}

function prepareCloneFields(number, wrapperNode) {
  wrapperNode.querySelectorAll('label')?.forEach((el) => {
    let forVal = el.getAttribute('for');
    el.setAttribute('for', forVal.replace(/-\d*-/, `-${number}-`));
  });

  wrapperNode.querySelectorAll('input')?.forEach((el) => {
    let nameVal = el.getAttribute('name');
    el.setAttribute('name', nameVal.replace(/\[\d*\]/, `[${number}]`));
    el.id = el.id.replace(/-\d*-/, `-${number}-`);
  });

  wrapperNode.querySelectorAll('select')?.forEach((el) => {
    let nameVal = el.getAttribute('name');
    el.setAttribute('name', nameVal.replace(/\[\d*\]/, `[${number}]`));
    el.id = el.id.replace(/-\d*-/, `-${number}-`);
  });

  let smSelect = wrapperNode.querySelector('.js-sm-choice');
  if (smSelect) {
    prepareSmSelect(smSelect);
  }

  return wrapperNode;
}

function allCloneInit() {
  let formCloneBtn = document.querySelectorAll('.js-form-clone-btn');

  formCloneBtn?.forEach((el) => {
    let { cloneTarget, cloneRemoveOriginal } = el.dataset;
    let targetEl = document.querySelector(cloneTarget);

    let cloneOptions = {
      remove: [],
    };

    if (!targetEl?.initalNode) {
      targetEl.initialNode = targetEl.cloneNode(true);
      targetEl.classList.add('form-clone');
    }

    if (cloneRemoveOriginal) {
      targetEl.innerHTML = '';
    }

    el.addEventListener('click', (e) => {
      e.preventDefault();
      cloneFormGroup(cloneTarget, cloneOptions);
      updateCloneBtn(el);
      setSmsPlaceholders();
      previewHide();
    });
  });

  let formCloneRemoveBtn = document.querySelectorAll(
    '.js-form-clone-remove'
  );
  formCloneRemoveBtn?.forEach(cloneRemoveBtnInit);
}

function updateCloneBtn(cloneBtn) {
  let { cloneTarget, cloneMaxItems = Infinity } = cloneBtn.dataset;
  let targetEl = document.querySelector(cloneTarget);

  if (
    Number(cloneMaxItems) <=
    targetEl.parentElement.querySelectorAll('.form-clone > *:first-child')
      .length
  ) {
    cloneBtn.setAttribute('disabled', true);
  } else {
    cloneBtn.removeAttribute('disabled');
  }
}

function cloneRemoveBtnInit(btn) {
  btn.addEventListener('click', (e) => {
    let formClone = btn.closest('.form-clone');
    let cloneBtn =
      formClone.parentNode.parentNode.querySelector('.js-form-clone-btn');
    formClone.innerHTML = '';

    allSelectInit();
    updateCloneBtn(cloneBtn);
    previewHide();
  });
}

function handleFormSubmit(e) {
  let previewContainer = document.querySelector('.preview-container');

  if (validateForm()) {
    setTimeout(() => {
      previewShow();
      scrollTo(previewContainer);
    }, 300)
  } else {
    e.preventDefault();
    previewHide();
  }
}

function manualHide() {
  let installationGuideEl = document.querySelector('.js-installation-guide');
  installationGuideEl.classList.add('hidden');
}

function manualShow() {
  let installationGuideEl = document.querySelector('.js-installation-guide');
  let emailClientEl = document.querySelector('.js-ec-choice');

  let { manual } = ecDropdownData.find(o => o.value === emailClientEl.value) || {};
  if (!manual) {
    console.warn('Manual not found for email client', emailClientEl.value);
    manualHide();
    return;
  }

  installationGuideEl.replaceChildren(buildOlList(manual))
  installationGuideEl.classList.remove('hidden');
}

function previewHide() {
  let previewContainer = document.querySelector('.preview-container');
  previewContainer?.classList.add('hidden');
}

function previewShow() {
  applyPreviewOptions();
  manualShow();

  let previewContainer = document.querySelector('.preview-container');
  previewContainer?.classList.remove('hidden');

  let iframe = document.querySelector('.preview-iframe');
  let iframeDoc = iframe.contentWindow.document;
  iframe.style.height =
    (iframeDoc.body.scrollHeight || 150) + 16 + 'px';
}

function applyPreviewOptions() {
  let copyBtn = document.querySelector('.js-signature-copy');
  let copyHtmlBtn = document.querySelector('.js-signature-copy-html');
  let downloadBtn = document.querySelector('.js-signature-download');

  // Default settings
  copyBtn.style.display = '';
  copyHtmlBtn.style.display = '';
  downloadBtn.style.display = 'none';

  // Custom settings
  let clientsOptions = {
    'native-mac': {
      hideCopyBtn: true,
      hideCopyHtmlBtn: true,
      showDownloadBtn: true
    },
  }

  let emailClient = document.getElementById('email-client')?.value;
  let clientOptions = clientsOptions[emailClient];

  if (clientOptions) {
    if (clientOptions.hideCopyBtn) {
      copyBtn.style.display = 'none';
    } else {
      copyBtn.style.display = '';
    }

    if (clientOptions.hideCopyHtmlBtn) {
      copyHtmlBtn.style.display = 'none';
    } else {
      copyBtn.style.display = '';
    }

    if (clientOptions.showDownloadBtn) {
      prepareDownloadBtn();
      downloadBtn.style.display = '';
    } else {
      copyBtn.style.display = 'none';
    }
  }
}

function prepareDownloadBtn() {
  let form = document.querySelector('form');
  let downloadBtn = document.querySelector('.js-signature-download');
  let formDataEntries = new FormData(form).entries();

  let params = new URLSearchParams();
  for (const [name, value] of formDataEntries) {
    params.append(name, value);
  }

  downloadBtn.href = `/v3/signature-eml?${params.toString()}`;
}

// Chars counter
function allMaxCharsCounterInit() {
  document.querySelectorAll('.js-input-maxlen')?.forEach((el) => {
    let charsCounterClass = 'input-chars-counter';
    let charsCounterEl =
      el.parentElement.getElementsByClassName(charsCounterClass)[0];

    if (!charsCounterEl) {
      charsCounterEl = document.createElement('span');
      charsCounterEl.className = charsCounterClass;
      el.parentElement.insertBefore(charsCounterEl, el);
    }

    charsCounterEl.innerText = `${el.value.length}/${el.maxLength}`;

    el.addEventListener(
      'input',
      (e) =>
        (charsCounterEl.innerText = `${el.value.length}/${el.maxLength}`)
    );
  });
}


// ChoicesJS
function selectInit(el, customOptions = {}) {
  let choicesCount = el.options.length;
  let elementId = el.id;

  el.originalInnerHTML = el.innerHTML;
  el.choices = new Choices(el, {
    searchEnabled: false,
    callbackOnCreateTemplates: function (template) {
      let classNames = this.config.classNames;
      let itemSelectText = this.config.itemSelectText;

      return {
        item: ({ classNames }, data) => {
          const { customProperties: iconData, label } = data;
          return template(`
              <div
                class="
                  ${data.highlighted
              ? classNames.highlightedState
              : classNames.itemSelectable
            }
                  ${data.placeholder ? classNames.placeholder : ''}
                "
                data-item
                data-id="${data.id}"
                data-value="${data.value}"
                ${data.active ? 'aria-selected="true"' : ''}
                ${data.disabled ? 'aria-disabled="true"' : ''}
              >
              ${iconData ? `<img class="select-item-icon" width="24" height="24" src="${String(
              iconData
            )}" alt="Icon ${label}" />` : ``}
              ${elementId === 'email-client' ? `<span class='choices__item--label'>${label}</span>` : ''}
              </div>
            `);
        },
        choice: ({ classNames }, data) => {
          const { customProperties: iconData, label } = data;
          return template(`
              <div
                class="${classNames.item}"
                data-select-text="${itemSelectText}"
                data-choice
                data-id="${data.id}"
                data-value="${data.value}"
                ${data.disabled
              ? 'data-choice-disabled aria-disabled="true"'
              : 'data-choice-selectable'
            }
                id="${data.elementId}"
              >
                ${iconData ? `<img class="select-choice-icon" width="24" height="24" src="${String(
              iconData
            )}" alt="Icon ${label}">` : ``}
                ${String(data.label)}
              </div>
            `);
        },
      };
    },
    ...customOptions
  });

  el.addEventListener('change', () => {
    removeAnyNullOption(el.choices.choiceList.element.children);
  });
  removeAnyNullOption(el.choices.choiceList.element.children);

  if (choicesCount < 2) {
    el.closest('.choices').classList.add('is-disabled');
  }

}

function removeAnyNullOption(optionElements) {
  for (const optionElement of optionElements) {
    if (optionElement.dataset.value === 'null') {
      optionElement.remove();
    }
  }
}


function allSelectInit() {
  let selectEls = document.querySelectorAll('.js-choice');
  selectEls.forEach((select) => {
    if (!select.choices) {
      selectInit(select);
    }
  });

  let ecSelectEls = document.querySelectorAll('.js-ec-choice');
  ecSelectEls.forEach((select) => {
    if (!select.choices) {
      selectInit(select, {
        shouldSort: false
      });
    }
  });

  prepareSmSelects();
  let smSelectEls = document.querySelectorAll('.js-sm-choice');
  smSelectEls.forEach(select => {
    selectInit(select);
  })
}

function prepareSmSelects() {
  let smSelectEls = document.querySelectorAll('.js-sm-choice');
  smSelectEls.forEach(prepareSmSelect)
}

function prepareSmSelect(select) {
  let smSelectEls = document.querySelectorAll('.js-sm-choice');
  let selectedSms = getSelectedSms();
  let selectedVal = select.value;
  let originalSelect = document.querySelector('.js-form-sm').initialNode.querySelector('.js-sm-choice');

  if (select.choices) {
    select.choices.destroy();
  }

  select.innerHTML = originalSelect.innerHTML;
  select.value = selectedVal;

  selectedSms?.forEach(selectedSm => {
    let isUnique = [...smSelectEls].find(select => select.value === selectedSm) === select;
    let selectedOptionEl = select.querySelector(`option[value="${selectedSm}"]`);
    if (!selectedOptionEl || isUnique) return;
    selectedOptionEl.remove();
  })
}

function getSelectedSms() {
  let form = document.querySelector('form');
  let formDataEntries = new FormData(form).entries();

  let selectedSms = [];
  for (const [key, value] of formDataEntries) {
    if (/sm\[\d\]\[icon\]/.test(key)) {
      selectedSms.push(value);
    }
  }

  return selectedSms;
}


// Copy button
function copyIframeContent(iframe) {
  const iframeHtmlEl = iframe.contentWindow.document.querySelector('html');
  navigator.clipboard.write([new ClipboardItem({
    'text/plain': new Blob([iframeHtmlEl.innerText], { type: 'text/plain' }),
    'text/html': new Blob([iframeHtmlEl.outerHTML], { type: 'text/html' })
  })])
}

function copyIframeContentLegacy(iframe) {
  let docHtml = iframe.contentWindow.document.body.innerHTML;
  let tempEl = document.createElement('div');

  tempEl.innerHTML = docHtml;
  iframe.parentNode.appendChild(tempEl)

  let range = document.createRange();
  range.selectNodeContents(tempEl);

  let selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
  document.execCommand('copy');
  tempEl.remove();
}

function copyIframeHtml(iframe) {
  let iframeHtml = iframe.contentWindow.document.querySelector('html')?.innerHTML;
  navigator.clipboard.writeText(iframeHtml);
}

function signatureCopyInit() {
  let btn = document.querySelector('.js-signature-copy');
  let iframe = document.querySelector('.preview-iframe');

  btn.addEventListener('click', async (e) => {
    let isFirefox = getUserAgent().includes('firefox');

    await iframePrepare();

    if (isFirefox) {
      copyIframeContentLegacy(iframe);
    } else {
      copyIframeContent(iframe);
    }

    setBtnActionText(btn, 'Copied!');
  });
}

function signatureCopyHtmlInit() {
  let btn = document.querySelector('.js-signature-copy-html');
  let iframe = document.querySelector('.preview-iframe');

  btn.addEventListener('click', (e) => {
    copyIframeHtml(iframe);
    setBtnActionText(btn, 'Copied!');
  });
}

function setBtnActionText(btn, text) {
  let btnTextEl = btn.querySelector('span');
  let btnOriginalText = btn.dataset.originalText || btnTextEl.innerText;

  btn.disabled = true;
  btn.dataset.originalText = btnOriginalText;
  btnTextEl.innerText = text;

  btnTextEl.textTimeout = setTimeout(() => {
    btnTextEl.innerText = btnOriginalText;
    btn.disabled = false;
  }, 1000);
}

async function iframePrepare(options = {}) {
  let iframe = document.querySelector('.preview-iframe');
  let iframeDoc = iframe.contentWindow.document;

  let anchors = iframeDoc.querySelectorAll('a');
  anchors?.forEach((anchor) => anchor.setAttribute('target', '_blank'));
}

function handleChangePhoneNumber(phoneEl) {
  let phoneVal = phoneEl.value;
  phoneEl.value = phoneVal.replace(/[^\d\+]/g, '');
}

function formInit() {
  let formEl = document.querySelector('form');
  formEl.addEventListener('submit', handleFormSubmit);
}

function onSmSelectChangeInit() {
  let smSelects = document.querySelectorAll('select[name^=sm]');
  smSelects.forEach((smSelect) =>
    smSelect.addEventListener('change', (e) => {
      setSmPlaceholder(smSelect);
      previewHide();
    })
  );
}

function setSmPlaceholder(smSelect) {
  let linkFieldName = smSelect.name.replace('icon', 'link');
  let linkField = document.querySelector(`[name="${linkFieldName}"]`);

  if (smSelect.value === 'linkedin') {
    linkField.placeholder = 'https://www.linkedin.com/in/username/';
  } else if (smSelect.value === 'x') {
    linkField.placeholder = 'https://x.com/profile';
  } else if (smSelect.value === 'github') {
    linkField.placeholder = 'https://github.com/username';
  }
}

function setSmsPlaceholders() {
  let smSelects = document.querySelectorAll('select[name^=sm]');
  smSelects?.forEach(smSelect => setSmPlaceholder(smSelect))
}

function previewHideOnInputInit() {
  let formEl = document.querySelector('form');
  formEl.addEventListener('change', () => previewHide());
}

// Email client dropdown data init
function emailClientDropdownDataInit() {
  const emailClientEl = document.querySelector('.js-ec-choice');

  if (!emailClientEl) { return };

  emailClientEl.options.length = 0

  ecDropdownData.map(({ value, img, label }) => {
    let option = document.createElement("option");
    option.value = value;
    option.setAttribute('data-custom-properties', img);
    option.append(label);
    emailClientEl.append(option);
  })
}

// Utilities
function isMobile() {
  return /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent);
}

function getUserAgent() {
  return navigator.userAgent.toLowerCase();
}

function scrollTo(el) {
  el.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function getQueryParam(name) {
  let queryString = window.location.search;
  let urlParams = new URLSearchParams(queryString);
  return urlParams.get(name);
}

async function toDataURL(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.onload = function () {
      if (this.status >= 200 && this.status < 300) {
        const reader = new FileReader();
        reader.onloadend = function () {
          resolve(reader.result);
        };
        reader.readAsDataURL(xhr.response);
      }
    };
    xhr.open('GET', url);
    xhr.responseType = 'blob';
    xhr.send();
  });
}

function buildOlList(arrayOfStrings) {
  const list = document.createElement('ol');
  for (const string of arrayOfStrings) {
    const li = document.createElement('li');
    li.innerHTML = string;
    list.appendChild(li);
  }
  return list;
}


(() => {
  emailClientDropdownDataInit();
  allCloneInit();
  allSelectInit();
  allMaxCharsCounterInit();
  signatureCopyInit();
  signatureCopyHtmlInit();
  formInit();
  onSmSelectChangeInit();
  previewHideOnInputInit();
})();
