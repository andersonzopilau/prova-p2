$(document).ready(function()){

    $('.edit-event').click(function()){

        let values = this.id.split('-');
        $('#editInputId').prop('value', values[1]);
        $('#editInputEvent').prop('value', this.text);
        $('#editInputPriority').prop('value', values[2]);

        $('#editEvent').modal('toggle');

    }
}