# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Show.country'
        db.add_column('market_buy_show', 'country', self.gf('django.db.models.fields.CharField')(default='US', max_length=128), keep_default=False)

        # Adding field 'Show.location'
        db.add_column('market_buy_show', 'location', self.gf('django.db.models.fields.CharField')(default='49.00, -96.00', max_length=255), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Show.country'
        db.delete_column('market_buy_show', 'country')

        # Deleting field 'Show.location'
        db.delete_column('market_buy_show', 'location')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'inventory.product': {
            'Meta': {'object_name': 'Product'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketCategory']"}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shops.Shop']"}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketSubCategory']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.ProductType']", 'null': 'True', 'blank': 'True'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'default': "'0'", 'max_digits': '11', 'decimal_places': '2'})
        },
        'inventory.producttype': {
            'Meta': {'object_name': 'ProductType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'market.marketcategory': {
            'Meta': {'object_name': 'MarketCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '60', 'db_index': 'True'})
        },
        'market.marketplace': {
            'Meta': {'object_name': 'MarketPlace'},
            'base_domain': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '128'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '92'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '92', 'db_index': 'True'}),
            'template_prefix': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '92', 'db_index': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '92'})
        },
        'market.marketsubcategory': {
            'Meta': {'unique_together': "(('parent', 'slug'),)", 'object_name': 'MarketSubCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'subcategories'", 'null': 'True', 'to': "orm['market.MarketCategory']"}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '60', 'db_index': 'True'})
        },
        'market_buy.bestseller': {
            'Meta': {'object_name': 'BestSeller'},
            'from_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'revenue': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shops.Shop']"}),
            'to_date': ('django.db.models.fields.DateTimeField', [], {})
        },
        'market_buy.dealerpick': {
            'Meta': {'object_name': 'DealerPick'},
            'description': ('django.db.models.fields.TextField', [], {'default': "'Dealer description here'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'shop': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['shops.Shop']"})
        },
        'market_buy.editorpick': {
            'Meta': {'object_name': 'EditorPick'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Product']"})
        },
        'market_buy.marketplacepick': {
            'Meta': {'object_name': 'MarketPlacePick'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '5'}),
            'product': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['inventory.Product']"})
        },
        'market_buy.show': {
            'Meta': {'object_name': 'Show'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'admission': ('django.db.models.fields.DecimalField', [], {'default': "'0.0'", 'max_digits': '11', 'decimal_places': '2'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'contact_info': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'US'", 'max_length': '128'}),
            'date_from': ('django.db.models.fields.DateField', [], {}),
            'date_to': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'49.00, -96.00'", 'max_length': '255'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'time_from': ('django.db.models.fields.TimeField', [], {}),
            'time_to': ('django.db.models.fields.TimeField', [], {}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'market_buy.wishlistitem': {
            'Meta': {'object_name': 'WishListItem'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketCategory']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ideal_price': ('django.db.models.fields.DecimalField', [], {'max_digits': '11', 'decimal_places': '2'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'posted_by': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'posted_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketSubCategory']"})
        },
        'shops.shop': {
            'Meta': {'object_name': 'Shop'},
            'admin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'bids': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'date_time': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'default': "'39.29038,-76.61219'", 'max_length': '255'}),
            'marketplace': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['market.MarketPlace']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'views': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['market_buy']
