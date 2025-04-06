{% extends 'evalinstructor/layout.html' %}
{% block title %} {{title}} {% endblock %}
{% load static %}
{% block content %}

<div class="col-7 mx-auto mt-4 c">
    <div class="row">
        <div class="col-md-6 mb-4"> 
            <div class="card2 p-3">
                <div class="card-body">
                <h5 class="card-title">INFORMACION DEL INSTRUCTOR</h5>
                    <p>Nombres: {{ instructor.3 }}</p>
                    <p>Apellidos: {{ instructor.4 }}</p>
                    <p>Programa de Formacion: {{ instructor.2 }}</p>
                </div>
            </div>
        </div>
        <div class="col-md-6 mb-4"> 
            <div class="card2 p-3">
                <div class="card-body">
                <h5 class="card-title">INFORMACION DEL APRENDIZ</h5>
                    <p>Nombres: {{ aprendiz.2 }}</p>
                    <p>Apellidos: {{ aprendiz.3 }}</p>
                </div>
            </div>
        </div>
    </div>

    <div class="card2 pb-5 mx-auto"> 
        <form name="mio"  action="{% url 'guardar_respuestas' instructor.6 aprendiz.1 %}" method="POST">
        {% csrf_token %}
        <input type="hidden" id="aprendiz" name="aprendiz" value="{{ aprendiz.1 }}">
        <div class="col-12 mx-auto p-3 ">
            <br>
            <h2>Cuestionario de evaluación de instructores</h2>
            <h5>Tenga en cuenta que 1 esta en desacuerdo y 5 esta de acuerdo</h5>
            {% for pregunta in preguntas %}
            <script>
                function Ir(){
                    if(confirm("Esta seguro de Enviar?")){
                        x=document.getElementsByName("mio")
                        x[0].submit()
                    }
                }
            </script>
            <div class="card-body">
                <div class="form-group">
                    <p class="c">{{ pregunta.0 }}. {{ pregunta.1 }}</p> 
                    <div class="col-lg-6 col-sm-10 mx-auto backspick p-2 c">
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="{{ pregunta.0 }}" id="inlineRadio1" value="1" checked>
                            <label class="form-check-label" for="inlineRadio1">1</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="{{ pregunta.0 }}" id="inlineRadio2" value="2">
                            <label class="form-check-label" for="inlineRadio2">2</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="{{ pregunta.0 }}" id="inlineRadio3" value="3">
                            <label class="form-check-label" for="inlineRadio3">3</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="{{ pregunta.0 }}" id="inlineRadio4" value="4">
                            <label class="form-check-label" for="inlineRadio4">4</label>
                        </div>
                        <div class="form-check form-check-inline">
                            <input class="form-check-input" type="radio" name="{{ pregunta.0 }}" id="inlineRadio5" value="5">
                            <label class="form-check-label" for="inlineRadio5">5</label>
                        </div>
                    </div>
                </div> 
            </div> 
            {% endfor %}
            <div>
                <br>
                <!-- <input type="submit" class="btn btn-primary mt-4" value="ENVIAR" /> -->
                <a href="javascript:Ir()" class="btn btn-primary btn-block">Enviar</a>
                <a href="javascript:goBack()" class="btn btn-primary btn-block">Cancelar</a>

        </form>
                <!-- <button class="btn btn-secondary btn-block" onclick="goBack()">Cancel</button> -->
        </div>  
    </div>

</div>
<script>
    function goBack() {
    window.history.back();
    }

</script>
{% endblock %}