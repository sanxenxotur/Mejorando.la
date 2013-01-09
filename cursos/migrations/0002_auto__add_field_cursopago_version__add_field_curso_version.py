# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CursoPago.version'
        db.add_column('cursos_cursopago', 'version',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)

        # Adding field 'Curso.version'
        db.add_column('cursos_curso', 'version',
                      self.gf('django.db.models.fields.IntegerField')(default=1),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CursoPago.version'
        db.delete_column('cursos_cursopago', 'version')

        # Deleting field 'Curso.version'
        db.delete_column('cursos_curso', 'version')


    models = {
        'cursos.curso': {
            'Meta': {'object_name': 'Curso'},
            'activado': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'info_pago': ('django.db.models.fields.TextField', [], {}),
            'mapa': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'precio': ('django.db.models.fields.IntegerField', [], {}),
            'slug': ('django.db.models.fields.TextField', [], {}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'cursos.cursodia': {
            'Meta': {'object_name': 'CursoDia'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cursos.Curso']"}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tema': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'temario': ('django.db.models.fields.TextField', [], {})
        },
        'cursos.cursodocente': {
            'Meta': {'object_name': 'CursoDocente'},
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cursos.Curso']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'perfil': ('django.db.models.fields.TextField', [], {}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'cursos.cursopago': {
            'Meta': {'object_name': 'CursoPago'},
            'charged': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'curso': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cursos.Curso']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'error': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'pais': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'version': ('django.db.models.fields.IntegerField', [], {'default': '1'})
        },
        'cursos.cursoregistro': {
            'Meta': {'object_name': 'CursoRegistro'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pago': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cursos.CursoPago']"})
        }
    }

    complete_apps = ['cursos']