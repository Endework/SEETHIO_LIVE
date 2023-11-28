
"use strict";

class Popup {
constructor(settings) {
this.className = settings.className ? settings.className : '';
this.containerClasses = settings.containerClasses ? settings.containerClasses : '';
this.onOpen = settings.onOpen && typeof settings.onOpen === 'function' ? settings.onOpen : null;
this.onClose = settings.onClose && typeof settings.onClose === 'function' ? settings.onClose : null;

this.el = document;
this.popup = document.querySelector('.popup');
}

open(fn) {
this.popup.classList.add('active');
if (this.onOpen) this.onOpen();
}

close(fn) {
this.popup.classList.remove('active');
if (this.onClose) this.onClose();
}
}

class Cropper {
constructor(el, settings = {}) {
this.options = {
    aspectRatio: '.aspect-ratio',
    imageBox: '.image-box',
    thumbBox: '.thumb-box',
    spinner: '.spinner',
    imgSrc: 'ID_Photo.png',
}

this.settings = {
    className: settings.className
}

this.el = document;
this.cropper;
this.blobImageInput;
this.base64ImageInput;
this.blobImageOutput;
this.base64ImageOutput;
this.filename;
this.fileInput = this.el.querySelector('.file-input');
this.fileButton = this.el.querySelector('.file-button');
this.zoomSlider = this.el.querySelector('.zoom-slider');
this.cancelButton = this.el.querySelector('.cancel-button');
this.saveButton = this.el.querySelector('.crop-button');
this.removeButton = this.el.querySelector('.remove-button');
this.cropResult = this.el.querySelector('.crop-result');
this.croppedImage = this.el.querySelector('.crop-result .image');
this.croppedImageName = this.el.querySelector('.crop-result .name');

this.popup = new Popup({
    className: 'popup--profile-crop ' + this.settings.className,
    containerClasses: this.settings.containerClasses,
    onClose: this.closeCropImageEvent
});

this.fileInput.addEventListener('change', this.fileInputChange.bind(this));
this.fileButton.addEventListener('click', this.fileButtonClick.bind(this));
this.zoomSlider.addEventListener('input', this.zoomSlide.bind(this));
this.cancelButton.addEventListener('click', this.cancelCrop.bind(this));
this.saveButton.addEventListener('click', this.saveCrop.bind(this));

if (this.removeButton) {
    this.removeButton.addEventListener('click', this.removeCrop.bind(this));
    this.displayCropResult();
}
}

displayCropResult() {
this.cropResult && this.filename && this.blobImageOutput ? this.cropResult.classList.add('active') : this.cropResult.classList.remove('active');
}

removeCrop() {
this.filename = "";
this.blobImageOutput = null;
this.base64ImageOutput = null;

if (this.croppedImage && this.croppedImageName) {
    this.croppedImage.innerHTML = '';
    this.croppedImageName.innerHTML = this.filename;
    this.displayCropResult();
}
}

fileInputChange() {
let reader = new FileReader();
this.filename = Math.random().toString(36).substring(2, 10) + Math.random().toString(36).substring(2, 10) + ".png";

reader.onload = (ev) => {
    this.blobImageInput = this.fileInput.files[0];
    this.base64ImageInput = ev.target.result;

    this.options.imgSrc = ev.target.result;
    this.cropper = this.cropbox(this.options);
    // init cropper zoom with value set on input
    this.cropper.zoom(this.zoomSlider.value);

    // emit the submitImageToCrop event
    this.submitFileInputEvent(this.el);
    this.openPopup();
}

if (this.fileInput.files[0]) {
    reader.readAsDataURL(this.fileInput.files[0]);
    this.fileInput.fileList = [];
}
}

openPopup() {
this.popup.open();
}

closePopup() {
this.popup.close();
}

fileButtonClick() {
this.fileInput.click();
}

zoomSlide() {
this.cropper.zoom(this.zoomSlider.value);
}

cancelCrop() {
this.fileInput.value = null;
this.blobImageInput = null;
this.base64ImageInput = null;
this.displayCropResult();
this.cancelCropImageEvent(this.el);
this.popup.close();
}

saveCrop() {
this.fileInput.value = null;
this.blobImageInput = null;
this.base64ImageInput = null;
this.blobImageOutput = this.cropper.getBlob();
this.base64ImageOutput = this.cropper.getDataURL();

if (this.croppedImage && this.croppedImageName) {
    this.croppedImage.innerHTML = '<img src="' + this.base64ImageOutput + '">';
    this.croppedImageName.innerHTML = this.filename;
    this.displayCropResult();
}

// emit the saveCropImage event
this.saveCropImageEvent(this.el);
this.popup.close();
}

// emit a file submit event
submitFileInputEvent(e) {
const event = new CustomEvent('submitImageToCrop', {
    detail: [{
            label: 'base64',
            value: this.base64ImageInput
        },
        {
            label: 'blob',
            value: this.blobImageInput
        }
    ],
})
e.dispatchEvent(event);
}

// emit a save event
saveCropImageEvent(e) {
const event = new CustomEvent('saveCropImage', {
    detail: [{
            label: 'base64',
            value: this.cropper.getDataURL()
        },
        {
            label: 'blob',
            value: this.cropper.getBlob()
        }
    ]
})
e.dispatchEvent(event);
}

// emit a cancel event
cancelCropImageEvent(e) {
const event = new CustomEvent('cancelCropImage', {
    detail: {
        canceled: true
    }
})
e.dispatchEvent(event);
}

// emit a close event
closeCropImageEvent(e) {
const event = new CustomEvent('closeCropImage', {
    detail: {
        closed: true
    }
})

const element = document.querySelector('.cropper');
element.dispatchEvent(event);
}

// lightweight image crop vanilla JS library
cropbox(options) {
let el = document.querySelector(options.imageBox),
    obj = {
        state: {},
        ratio: 1,
        options: options,
        imageBox: el,
        thumbBox: el.querySelector(options.thumbBox),
        spinner: el.querySelector(options.spinner),
        aspectRatio: document.querySelector(options.aspectRatio),
        image: new Image(),
        getDataURL: function() {
            let width = this.thumbBox.clientWidth,
                height = this.thumbBox.clientHeight,
                canvas = document.createElement("canvas"),
                dim = el.style.backgroundPosition.split(' '),
                size = el.style.backgroundSize.split(' '),
                dx = parseInt(dim[0]) - el.clientWidth / 2 + width / 2,
                dy = parseInt(dim[1]) - el.clientHeight / 2 + height / 2,
                dw = parseInt(size[0]),
                dh = parseInt(size[1]),
                sh = parseInt(this.image.height),
                sw = parseInt(this.image.width);

            canvas.width = width;
            canvas.height = height;
            let context = canvas.getContext("2d");
            context.drawImage(this.image, 0, 0, sw, sh, dx, dy, dw, dh);
            let imageData = canvas.toDataURL('image/png');
            return imageData;
        },
        getBlob: function() {

            console.log(this)
            let imageData = this.getDataURL();
            let b64 = imageData.replace('data:image/png;base64,', '');
            let binary = atob(b64);
            let array = [];
            for (let i = 0; i < binary.length; i++) {
                array.push(binary.charCodeAt(i));
            }
            return new Blob([new Uint8Array(array)], { type: 'image/png' });
        },
        zoomIn: function() {
            this.ratio *= 1.1;
            setBackground();
        },
        zoomOut: function() {
            this.ratio *= 0.9;
            setBackground();
        },
        zoom: function(value) {
            // value: [-20, 20]
            this.ratio = 1 + value / 20;
            setBackground();
        }
    },
    attachEvent = function(node, event, cb) {
        if (node.attachEvent)
            node.attachEvent('on' + event, cb);
        else if (node.addEventListener)
            node.addEventListener(event, cb);
    },
    detachEvent = function(node, event, cb) {
        if (node.detachEvent) {
            node.detachEvent('on' + event, cb);
        } else if (node.removeEventListener) {
            node.removeEventListener(event, render);
        }
    },
    stopEvent = function(e) {
        if (window.event) e.cancelBubble = true;
        else e.stopImmediatePropagation();
    },
    setBackground = function() {
        // new image size
        let newImageWidth = parseInt((parseInt(obj.image.width) * obj.ratio).toFixed(2));
        let newImageHeight = parseInt(obj.image.height) * obj.ratio;

        // centered position
        let centerX = (el.clientWidth - newImageWidth) / 2;
        let centerY = (el.clientHeight - newImageHeight) / 2;

        // default position
        let newBgPositionX = centerX;
        let newBgPositionY = centerY;

        // get current background position
        if (el.style.backgroundSize && el.style.backgroundPosition) {
            // current image size
            let bgWidth = parseInt(el.style.backgroundSize.split(' ')[0]);
            let bgHeight = parseInt(el.style.backgroundSize.split(' ')[1]);

            // current image position
            let bgPositionX = parseInt(el.style.backgroundPosition.split(' ')[0]);
            let bgPositionY = parseInt(el.style.backgroundPosition.split(' ')[1]);

            // keep it default if no background position set
            if (bgPositionX !== 0 || bgPositionY !== 0) {
                // get prev. & new image size delta
                let imageWidthDelta = parseInt(Math.abs((newImageWidth - bgWidth) / 2).toFixed(2));
                let imageHeightDelta = parseInt(Math.abs((newImageHeight - bgHeight) / 2).toFixed(2));
                // get new bg position
                newBgPositionX = newImageWidth > bgWidth ? bgPositionX - imageWidthDelta : bgPositionX + imageWidthDelta;
                newBgPositionY = newImageHeight > bgHeight ? bgPositionY - imageHeightDelta : bgPositionY + imageHeightDelta;
            }
        }

        el.setAttribute('style',
            'background-image: url(' + obj.image.src + '); ' +
            'background-size: ' + newImageWidth + 'px ' + newImageHeight + 'px; ' +
            'background-position: ' + newBgPositionX + 'px ' + newBgPositionY + 'px; ' +
            'background-repeat: no-repeat');
    },
    ratioToPixel = function(ratio, mw, mh) {
        let wr = parseInt(ratio.split('/')[0]),
            hr = parseInt(ratio.split('/')[1]),
            w = 0,
            h = 0;

        if (wr <= hr) {
            w = mh / hr * wr;
            h = mh;

            if (w > mw) {
                h = h / w * mw;
                w = mw;
            }
        } else {
            w = mw;
            h = mw / wr * hr;

            if (h > mh) {
                w = w / h * mh;
                h = mh;
            }
        }

        return {
            width: w,
            height: h,
        }
    },
    setAspectRatio = function() {
        let { width, height } = ratioToPixel(obj.aspectRatio.value, obj.imageBox.offsetWidth - 20, obj.imageBox.offsetHeight - 20);

        let rect = obj.thumbBox.querySelector('rect');
        if (rect) {
            rect.style.width = width - 2 + 'px';
            rect.style.height = height - 2 + 'px';
            rect.style.x = 1 + 'px'
            rect.style.y = 1 + 'px'
        }

        obj.thumbBox.style.width = width + 'px';
        obj.thumbBox.style.height = height + 'px';
    },
    imgMouseDown = function(e) {
        stopEvent(e);

        obj.state.dragable = true;
        obj.state.mouseX = e.clientX;
        obj.state.mouseY = e.clientY;
    },
    imgMouseMove = function(e) {
        stopEvent(e);

        if (obj.state.dragable) {
            let x = e.clientX - obj.state.mouseX;
            let y = e.clientY - obj.state.mouseY;

            let bg = el.style.backgroundPosition.split(' ');

            let bgX = x + parseInt(bg[0]);
            let bgY = y + parseInt(bg[1]);

            el.style.backgroundPosition = bgX + 'px ' + bgY + 'px';

            obj.state.mouseX = e.clientX;
            obj.state.mouseY = e.clientY;
        }
    },
    imgMouseUp = function(e) {
        stopEvent(e);
        obj.state.dragable = false;
    },
    imgTouchStart = function(e) {
        stopEvent(e);

        let touch = e.touches[0];
        obj.state.dragable = true;
        obj.state.mouseX = touch.clientX;
        obj.state.mouseY = touch.clientY;
    },
    imgTouchMove = function(e) {
        stopEvent(e);

        if (obj.state.dragable) {
            let touch = e.touches[0];

            let x = touch.clientX - obj.state.mouseX;
            let y = touch.clientY - obj.state.mouseY;

            let bg = el.style.backgroundPosition.split(' ');

            let bgX = x + parseInt(bg[0]);
            let bgY = y + parseInt(bg[1]);

            el.style.backgroundPosition = bgX + 'px ' + bgY + 'px';

            obj.state.mouseX = touch.clientX;
            obj.state.mouseY = touch.clientY;
        }
    },
    imgTouchEnd = function(e) {
        stopEvent(e);
        obj.state.dragable = false;
    },
    zoomImage = function(e) {
        let evt = window.event || e;
        let delta = evt.detail ? evt.detail * (-120) : evt.wheelDelta;
        delta > -120 ? obj.ratio *= 1.1 : obj.ratio *= 0.9;
        setBackground();
    }

obj.spinner.style.display = 'block';
obj.image.onload = function() {
    obj.spinner.style.display = 'none';
    el.style.backgroundPosition = '0px 0px';

    setAspectRatio();
    setBackground();

    attachEvent(el, 'mousedown', imgMouseDown);
    attachEvent(el, 'mousemove', imgMouseMove);
    attachEvent(document.body, 'mouseup', imgMouseUp);
    attachEvent(el, 'touchstart', imgTouchStart);
    attachEvent(el, 'touchmove', imgTouchMove);
    attachEvent(document.body, 'touchend', imgTouchEnd);
    attachEvent(obj.aspectRatio, 'change', setAspectRatio);

    // remove the scroll zoom
    //  let mousewheel = (/Firefox/i.test(navigator.userAgent))? 'DOMMouseScroll' : 'mousewheel';
    //  attachEvent(el, mousewheel, zoomImage);
};
obj.image.src = options.imgSrc;
attachEvent(el, 'DOMNodeRemoved', function() { detachEvent(document.body, 'DOMNodeRemoved', imgMouseUp) });

return obj;
}
}

document.addEventListener("DOMContentLoaded", () => {
let cropper = new Cropper({});
});

