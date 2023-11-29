this.zoomSlider = this.el.querySelector('.zoom-slider');
this.zoomSlider.addEventListener('input', this.zoomSlide.bind(this));
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
zoomSlide() {
    this.cropper.zoom(this.zoomSlider.value);
    }