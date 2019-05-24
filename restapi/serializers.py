from rest_framework import serializers
from .models import Movies,Comments
import json
import urllib
class MoviesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields=('id','Title','Year','Rated','Released','Runtime','Genre','Director','Writer','Actors','Plot','Language','Country','Awards','Poster','Ratings','Metascore','imdbRating','imdbVotes','imdbID','Type','DVD','BoxOffice','Production','Website','totalSeasons','Response')
        read_only_fields=('id','Year','Rated','Released','Runtime','Genre','Director','Writer','Actors','Plot','Language','Country','Awards','Poster','Ratings','Metascore','imdbRating','imdbVotes','imdbID','Type','DVD','BoxOffice','Production','Website','totalSeasons','Response')
        model=Movies

    def string_factory(dicts, string):
        formatted = []
        for data in dicts:
            new_dict = data
            formatted.append(string.format(**new_dict))
        return formatted
    def create(self,validated_data):
        title=str(validated_data['Title'])
        req = urllib.request.Request("http://www.omdbapi.com/?apikey=525e3132&t="+title)
        opener = urllib.request.build_opener()
        f = opener.open(req)
        json_data = json.loads(f.read())
        print (json_data)
        try:
            assert json_data['Response'] != 'False'
        except AssertionError as e:
            raise(AssertionError('There is no such Movies in database'))
        for k, v in json_data.items():
            validated_data[k]=v
        return Movies.objects.create(**validated_data)
class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields=('Movie_ID','Context',)
        model=Comments
    def create(self,validated_data):
        try:
            obj = Movies.objects.get(id=validated_data['Movie_ID'])
        except Movies.DoesNotExist:
            obj=None
        try:
            assert None != obj
        except AssertionError as e:
            raise(AssertionError('There is no such id in the Movies database'))
        return Comments.objects.create(**validated_data)
    def get_queryset(self):
        id = self.request.id
        return Comments.objects.filter(Movie_ID=id)
class TopSerializer(serializers.Serializer):
    class Meta:
        fields=('Movie_ID','Rank','Comments count')