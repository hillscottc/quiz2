# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserProfile'
        db.create_table(u'quiz_userprofile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['UserProfile'])

        # Adding model 'Quiz'
        db.create_table(u'quiz_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quiz', ['Quiz'])

        # Adding unique constraint on 'Quiz', fields ['user', 'name']
        db.create_unique(u'quiz_quiz', ['user_id', 'name'])

        # Adding model 'QuizLog'
        db.create_table(u'quiz_quizlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Quiz'])),
            ('taker', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'quiz', ['QuizLog'])

        # Adding model 'RawLog'
        db.create_table(u'quiz_rawlog', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('message', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'quiz', ['RawLog'])

        # Adding model 'Question'
        db.create_table(u'quiz_question', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('quiz', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Quiz'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'quiz', ['Question'])

        # Adding unique constraint on 'Question', fields ['text', 'quiz']
        db.create_unique(u'quiz_question', ['text', 'quiz_id'])

        # Adding model 'Answer'
        db.create_table(u'quiz_answer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('correct', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'quiz', ['Answer'])

        # Adding unique constraint on 'Answer', fields ['question', 'text']
        db.create_unique(u'quiz_answer', ['question_id', 'text'])

        # Adding model 'Tag'
        db.create_table(u'quiz_tag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('text', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
        ))
        db.send_create_signal(u'quiz', ['Tag'])

        # Adding model 'QuestionTag'
        db.create_table(u'quiz_questiontag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('updated_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Question'])),
            ('tag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['quiz.Tag'])),
        ))
        db.send_create_signal(u'quiz', ['QuestionTag'])

        # Adding unique constraint on 'QuestionTag', fields ['question', 'tag']
        db.create_unique(u'quiz_questiontag', ['question_id', 'tag_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'QuestionTag', fields ['question', 'tag']
        db.delete_unique(u'quiz_questiontag', ['question_id', 'tag_id'])

        # Removing unique constraint on 'Answer', fields ['question', 'text']
        db.delete_unique(u'quiz_answer', ['question_id', 'text'])

        # Removing unique constraint on 'Question', fields ['text', 'quiz']
        db.delete_unique(u'quiz_question', ['text', 'quiz_id'])

        # Removing unique constraint on 'Quiz', fields ['user', 'name']
        db.delete_unique(u'quiz_quiz', ['user_id', 'name'])

        # Deleting model 'UserProfile'
        db.delete_table(u'quiz_userprofile')

        # Deleting model 'Quiz'
        db.delete_table(u'quiz_quiz')

        # Deleting model 'QuizLog'
        db.delete_table(u'quiz_quizlog')

        # Deleting model 'RawLog'
        db.delete_table(u'quiz_rawlog')

        # Deleting model 'Question'
        db.delete_table(u'quiz_question')

        # Deleting model 'Answer'
        db.delete_table(u'quiz_answer')

        # Deleting model 'Tag'
        db.delete_table(u'quiz_tag')

        # Deleting model 'QuestionTag'
        db.delete_table(u'quiz_questiontag')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'quiz.answer': {
            'Meta': {'unique_together': "(('question', 'text'),)", 'object_name': 'Answer'},
            'correct': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Question']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.question': {
            'Meta': {'unique_together': "(('text', 'quiz'),)", 'object_name': 'Question'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Quiz']"}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.questiontag': {
            'Meta': {'unique_together': "(('question', 'tag'),)", 'object_name': 'QuestionTag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Question']"}),
            'tag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Tag']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.quiz': {
            'Meta': {'unique_together': "(('user', 'name'),)", 'object_name': 'Quiz'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'quiz.quizlog': {
            'Meta': {'object_name': 'QuizLog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'quiz': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['quiz.Quiz']"}),
            'taker': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.rawlog': {
            'Meta': {'object_name': 'RawLog'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.tag': {
            'Meta': {'object_name': 'Tag'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'quiz.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        }
    }

    complete_apps = ['quiz']