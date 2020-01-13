<template>
     <div class="container">
        <div class="row">
            <div class="col-8 mx-auto">
                <div class="bg-faded rounded p-5">
                    <h2 class="section-heading mb-4">
                    <span class="section-heading-lower">Crear Cuenta</span>  
                    </h2>
                    <div class="stepwizard col-md-offset-3">
                        <div class="stepwizard-row setup-panel">
                        <div class="stepwizard-step">
                            <a href="#step-1" type="button" class="btn btn-primary btn-circle">1</a>
                            <p>Personal</p>
                        </div>
                        <div class="stepwizard-step">
                            <a href="#step-2" type="button" class="btn btn-default btn-circle" disabled="disabled">2</a>
                            <p>Cuenta</p>
                        </div>
                        <div class="stepwizard-step">
                            <a href="#step-3" type="button" class="btn btn-default btn-circle" disabled="disabled">3</a>
                            <p>Confirmar</p>
                        </div>
                        </div>
                    </div>
                    
                    <form role="form" action="" method="post">
                        <div class="row setup-content" id="step-1">
                        <div class="col-xs-6 col-md-offset-3">
                            <div class="col-md-12">
                            <div class="form-group">
                                <label class="control-label">Cedula</label>
                                <input  maxlength="100" type="text" class="form-control" placeholder="Ingrese Cédula"  />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Nombre</label>
                                <input  maxlength="100" type="text" class="form-control" placeholder="Ingrese Nombre"  />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Apellido</label>
                                <input maxlength="100" type="text" class="form-control" placeholder="Ingrese Apellido" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Email</label>
                                <input maxlength="100" type="text" required="required" class="form-control" placeholder="Ingrese Email" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Teléfono</label>
                                <input maxlength="100" type="text" class="form-control" placeholder="Ingrese Teléfono" />
                            </div>
                            <button class="btn btn-primary nextBtn pull-right" type="button" >Siguiente</button>
                            </div>
                        </div>
                        </div>
                        <div class="row setup-content" id="step-2">
                        <div class="col-xs-6 col-md-offset-3">
                            <div class="col-md-12">
                            <div class="form-group">
                                <label class="control-label">Usuario</label>
                                <input maxlength="200" type="text" required="required" class="form-control" placeholder="Ingrese Usuario" />
                            </div>
                            <div class="form-group">
                                <label class="control-label">Contraseña</label>
                                <input maxlength="200" type="text" required="required" class="form-control" placeholder="Ingrese Contraseña"  />
                            </div>
                            <button class="btn btn-primary nextBtn pull-right" type="button" >Siguiente</button>
                            </div>
                        </div>
                        </div>
                        <div class="row setup-content" id="step-3">
                        <div class="col-xs-6 col-md-offset-3">
                            <div class="col-md-12">
                                <br>
                            <button class="btn btn-success pull-right" type="submit">Registrar</button>
                            </div>
                        </div>
                        </div>
                    </form>
                </div>
            </div>    
        </div>
    </div>
</template>
 
<script>
    const $ = require('jquery')
    window.$ = $
    $(document).ready(function () {
        var navListItems = $('div.setup-panel div a'),
          allWells = $('.setup-content'),
          allNextBtn = $('.nextBtn');

  allWells.hide();

  navListItems.click(function (e) {
      e.preventDefault();
      var $target = $($(this).attr('href')),
              $item = $(this);

      if (!$item.hasClass('disabled')) {
          navListItems.removeClass('btn-primary').addClass('btn-default');
          $item.addClass('btn-primary');
          allWells.hide();
          $target.show();
          $target.find('input:eq(0)').focus();
      }
  });

  allNextBtn.click(function(){
      var curStep = $(this).closest(".setup-content"),
          curStepBtn = curStep.attr("id"),
          nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]').parent().next().children("a"),
          curInputs = curStep.find("input[type='text'],input[type='url']"),
          isValid = true;

      $(".form-group").removeClass("has-error");
      for(var i=0; i<curInputs.length; i++){
          if (!curInputs[i].validity.valid){
              isValid = false;
              $(curInputs[i]).closest(".form-group").addClass("has-error");
          }
      }

      if (isValid)
          nextStepWizard.removeAttr('disabled').trigger('click');
  });

  $('div.setup-panel div a.btn-primary').trigger('click');
}) 
    export default {
    
    data () {
        return {
        
        }
    }
       
}
</script> 

<style scoped>
#registrar{
    text-align: center
}
body {
    margin-top:40px;
}
.stepwizard-step p {
    margin-top: 10px;
}
.stepwizard-row {
    display: table-row;
}
.stepwizard {
    display: table;
    width: 50%;
    position: relative;
}
.stepwizard-step button[disabled] {
    opacity: 1 !important;
    filter: alpha(opacity=100) !important;
}
.stepwizard-row:before {
    top: 14px;
    bottom: 0;
    position: absolute;
    content: " ";
    width: 100%;
    height: 1px;
    background-color: #ccc;
    z-order: 0;
}
.stepwizard-step {
    display: table-cell;
    text-align: center;
    position: relative;
}
.btn-circle {
    width: 30px;
    height: 30px;
    text-align: center;
    padding: 6px 0;
    font-size: 12px;
    line-height: 1.428571429;
    border-radius: 15px;
}
</style>