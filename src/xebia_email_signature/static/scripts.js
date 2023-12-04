function validateForm() {
  let errors = [];
  let errorsEls = document.querySelectorAll('.error');
  errorsEls.forEach((error) => (error.innerHTML = ''));

  let nameEl = document.getElementById('full_name');
  if (nameEl.value.trim() === '') {
    errors.push({
      target: document.getElementById('full_name-error'),
      msg: 'Please enter your name',
      input: nameEl
    })
  }
  let emailEl = document.getElementById('email');
  if (!validateEmail(emailEl.value)) {
    errors.push({
      target: document.getElementById('email-error'),
      msg: 'Please enter a valid email address',
      input: nameEl
    })
  }

  let jobRoleEl = document.getElementById('job_role');
  if (jobRoleEl.value.trim() === '') {
    errors.push({
      target: document.getElementById('job_role-error'),
      msg: 'Please enter your role',
      input: nameEl
    })
  }

  let phoneEl = document.getElementById('phone');
  if (!validatePhoneNumber(phoneEl.value)) {
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
    if (ctaDescEl.value.length !== 0 && linkEl.value.length === 0) {
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
    if (ctaLinkEl.value.length !== 0 && descEl.value.length === 0) {
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

function scrollTo(el) {
  el.scrollIntoView({ behavior: 'smooth', block: 'center' });
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

function selectInit(el) {
  let choicesCount = el.options.length;

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
            <img class="select-item-icon" width="24" height="24" src="${String(
              iconData
            )}" alt="Icon ${label}">
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
                <img class="select-choice-icon" src="${String(
              iconData
            )}" alt="Icon ${label}">
                ${String(data.label)}
              </div>
            `);
        },
      };
    },
  });

  if (choicesCount < 2) {
    el.closest('.choices').classList.add('is-disabled');
  }
}

function allSelectInit() {
  let selectEls = document.querySelectorAll('.js-choice');
  selectEls.forEach((select) => {
    if (!select.choices) {
      selectInit(select);
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
    });
  });

  let formCloneRemoveBtn = document.querySelectorAll(
    '.js-form-clone-remove'
  );
  formCloneRemoveBtn?.forEach(cloneRemoveBtnInit);
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
  });
}

function handleFormSubmit(e) {
  let previewContainer = document.querySelector('.preview-container');

  if (validateForm()) {
    previewContainer?.classList.remove('hidden');
  } else {
    e.preventDefault();
    previewContainer?.classList.add('hidden');
  }
}

function copyIframeContent(iframe) {
  let doc = iframe.contentWindow.document;
  let range = doc.createRange();
  range.selectNodeContents(iframe.contentWindow.document);
  let select = iframe.contentWindow.getSelection();
  select.removeAllRanges();
  select.addRange(range);
  iframe.contentWindow.document.execCommand('copy');
  select.removeAllRanges();
}

function signatureCopyInit() {
  let btn = document.querySelector('.js-signature-copy');
  let iframe = document.querySelector('.preview-iframe');

  btn.addEventListener('click', (e) => {
    copyIframeContent(iframe);

    let btnTextEl = btn.querySelector('span');
    let btnOriginalText = btnTextEl.innerText;

    btnTextEl.innerText = 'Copied!';
    if (!btnTextEl.textTimeout) {
      btnTextEl.textTimeout = setTimeout(() => {
        btnTextEl.innerText = btnOriginalText;
      }, 3000);
    }
  });
}

async function toDataURL(url, callback) {
  var xhr = new XMLHttpRequest();
  xhr.onload = function () {
    var reader = new FileReader();
    reader.onloadend = function () {
      callback(reader.result);
    };
    reader.readAsDataURL(xhr.response);
  };
  xhr.open('GET', url);
  xhr.responseType = 'blob';
  xhr.send();
}

function iframePrepareInit() {
  let iframe = document.querySelector('.preview-iframe');
  iframe.addEventListener('load', () => {
    let iframeDoc = iframe.contentWindow.document;
    let anchors = iframeDoc.querySelectorAll('a');
    let images = iframeDoc.querySelectorAll('img');

    anchors?.forEach((anchor) => anchor.setAttribute('target', '_blank'));
    images?.forEach((img) => {
      toDataURL(img.src, (imageBase64) =>
        img.setAttribute('src', imageBase64)
      );
    });

    iframe.style.height =
      (iframeDoc.body.scrollHeight || 150) + 16 + 'px';
  });
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
    smSelect.addEventListener('change', (e) =>
      setSmPlaceholder(smSelect)
    )
  );
}

function setSmPlaceholder(smSelect) {
  let linkFieldName = smSelect.name.replace('icon', 'link');
  let linkField = document.querySelector(`[name="${linkFieldName}"]`);

  if (smSelect.value === 'linkedin') {
    linkField.placeholder = 'https://www.linkedin.com/in/username/';
  } else if (smSelect.value === 'x') {
    linkField.placeholder = 'https://x.com/profile';
  }
}

function setSmsPlaceholders() {
  let smSelects = document.querySelectorAll('select[name^=sm]');
  smSelects?.forEach(smSelect => setSmPlaceholder(smSelect))
}

(() => {
  allCloneInit();
  allSelectInit();
  allMaxCharsCounterInit();
  signatureCopyInit();
  iframePrepareInit();
  formInit();
  onSmSelectChangeInit();
})();