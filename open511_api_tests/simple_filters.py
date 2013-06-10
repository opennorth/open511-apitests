from lxml import etree

from open511_api_tests.base import BaseCase, NSMAP


class SimpleFiltersCase(BaseCase):

    @classmethod
    def setUpClass(cls):
        super(SimpleFiltersCase, cls).setUpClass()
        cls.load(DOC)

    def test_smoke(self):
        self.get_events()

    def test_status_filter(self):
        default = self.get_events()
        # import pdb; pdb.set_trace()
        active = self.get_events(status='ACTIVE')
        self.assertEquals(len(default.xpath('event')), 6)
        assert len(active.xpath('event')) == 6
        archived = self.get_events(status='ARCHIVED')
        assert not archived.xpath('//status[text()="ACTIVE"]')
        assert len(archived.xpath('event')) == 13
        all_ = self.get_events(status='ALL')
        assert len(all_.xpath('event')) == 19
        assert len(all_.xpath('//status[text()="ACTIVE"]')) == 6
        assert len(all_.xpath('//status[text()="ARCHIVED"]')) == 13


DOC = """
<open511 xmlns:atom="http://www.w3.org/2005/Atom" xmlns:gml="http://www.opengis.net/gml" xml:base="http://repentigny.open511.ca" version="v0">
  <event xml:lang="fr" id="29">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#232;te</description>
    <schedule>
      <start_date>2013-05-08</start_date>
      <end_date>2013-05-09</end_date>
    </schedule>
    <headline>Excavation d'&#233;gouts</headline>
    <severity>1</severity>
    <detour>Partage des deux voies de circulation en direction Ouest</detour>
    <roads>
      <road>
        <road_name>Iberville</road_name>
        <from>Bonaventure</from>
        <to>Bord-de-l'eau</to>
      </road>
    </roads>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.468033075299999,45.722562664000002 -73.467056751300007,45.723641236500001 -73.466262817399993,45.724540030999997</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="25">
    <status>ARCHIVED</status>
    <description>Bris d'aqueduc</description>
    <schedule>
      <start_date>2013-05-18</start_date>
      <end_date>2013-05-19</end_date>
    </schedule>
    <headline>Bris d'aqueduc</headline>
    <severity>1</severity>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.471326828000002,45.727479736900001</gml:coordinates>
      </gml:Point>
    </geography>
    <created>2013-05-24T13:14:21.688587+00:00</created>
    <updated>2013-05-24T14:58:00.671428+00:00</updated>
  </event>
  <event xml:lang="fr" id="31">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#232;te</description>
    <schedule>
      <start_date>2013-05-02</start_date>
      <end_date>2013-05-02</end_date>
    </schedule>
    <headline>Excavation d'&#233;gouts</headline>
    <severity>1</severity>
    <roads>
      <road>
        <road_name>Guy</road_name>
        <from>Boulevard L&#233;vesque</from>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.463430404700006,45.726509838299997</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="27">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#233;te de la rue</description>
    <schedule>
      <start_date>2013-05-13</start_date>
      <end_date>2013-05-13</end_date>
    </schedule>
    <headline>Excavation d'&#233;gouts</headline>
    <severity>1</severity>
    <detour>Rues avoisinantes</detour>
    <roads>
      <road>
        <road_name>Vaudreuil</road_name>
        <from>Varin</from>
        <to>Saint Vallier</to>
      </road>
    </roads>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.428947925599999,45.7592748426 -73.427553176900005,45.760816779700001 -73.426458835600002,45.761954492500003</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="26">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#233;te de la rue Lucerne</description>
    <schedule>
      <start_date>2013-05-16</start_date>
      <end_date>2013-05-16</end_date>
    </schedule>
    <headline>Excavation d'&#233;gouts</headline>
    <severity>1</severity>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.435567617399997,45.756804660199997</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="28">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#233;te</description>
    <schedule>
      <start_date>2013-05-09</start_date>
      <end_date>2013-05-10</end_date>
    </schedule>
    <headline>Nouveau service pluvial</headline>
    <severity>1</severity>
    <roads>
      <road>
        <road_name>Denis</road_name>
        <from>Camille</from>
        <to>Maurice</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.438807725900006,45.7519238573 -73.436930179599997,45.751152771199997 -73.436114788099999,45.7509581264</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="30">
    <status>ACTIVE</status>
    <description>Fermeture compl&#232;te en direction Nord</description>
    <schedule>
      <start_date>2013-05-06</start_date>
      <end_date>2013-05-31</end_date>
    </schedule>
    <headline>Travaux majeurs d'aqueduc</headline>
    <severity>3</severity>
    <detour>Emprunter les boulevards Beauchesne ou Iberville pour acc&#233;der &#224; l'Autoroute.</detour>
    <roads>
      <road>
        <road_name>Valmont</road_name>
        <from>Sartre</from>
        <to>Beauchesne</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.434033393899995,45.764619044600003 -73.4352564812,45.765142958399998 -73.436522483800005,45.765696804800001</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="24">
    <status>ARCHIVED</status>
    <description>Entrave avec circulation en alternance sur le Boul. Pierre-Le Gardeur pr&#232;s de Place Aubert</description>
    <schedule>
      <start_date>2013-05-23</start_date>
      <end_date>2013-05-24</end_date>
    </schedule>
    <headline>Train de l'Est (NUIT)</headline>
    <severity>1</severity>
    <detour>Circulation en alternance avec signaleur</detour>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.485960960400007,45.737728176700003</gml:coordinates>
      </gml:Point>
    </geography>
    <roads>
      <road>
        <road_name>Boulevard Pierre-Le Gardeur</road_name>
        <from>Place Aubert</from>
      </road>
    </roads>
  </event>
  <event xml:lang="fr" id="33">
    <status>ARCHIVED</status>
    <description>Fermeture partiel de la rue Notre Dame:
- Fermeture de deux voies sur la rue Notre-Dame en face du num&#233;ro civique 915
- Maintien d&#8217;une voie de circulation dans chacune des directions en face du num&#233;ro civique 915</description>
    <schedule>
      <start_date>2013-05-27</start_date>
      <end_date>2013-05-27</end_date>
    </schedule>
    <headline>Travaux majeurs de branchement de services</headline>
    <severity>2</severity>
    <roads>
      <road>
        <road_name>Notre-Dame</road_name>
        <from>915 Notre-Dame</from>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.418304920200001,45.767433152499997</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="32">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#232;te de la rue Notre-Dame &#224; l'intersection des rues Gravel et Beauchesne. 
 - &#192; l&#8217;est de la rue Gravel, maintien de la circulation locale sur la rue Notre-Dame jusqu&#8217;&#224; la rue du Vieux Moulin et le 915 Notre-Dame. 
 - &#192; l&#8217;ouest de la rue Beauchesne, maintien de la circulation locale sur la rue Notre-Dame jusqu&#8217;au 915 Notre-Dame.</description>
    <schedule>
      <start_date>2013-05-25</start_date>
      <end_date>2013-05-25</end_date>
    </schedule>
    <headline>Travaux majeurs de branchement de services</headline>
    <severity>3</severity>
    <roads>
      <road>
        <road_name>Rue Notre-Dame</road_name>
        <from>Beauchesne</from>
        <to>Valmont</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.420965671499999,45.764244817399998 -73.419249057800002,45.766160834099999 -73.418433666200002,45.767058944200002 -73.417789936099993,45.767807358299997 -73.417446613300001,45.768181561600002 -73.417103290599997,45.768555762399998</gml:coordinates>
      </gml:LineString>
    </geography>
    <detour>Via la rue Beauchesne, le boulevard Iberville et la rue Gravel</detour>
  </event>
  <event xml:lang="fr" id="34">
    <status>ARCHIVED</status>
    <description>Fermeture partiel de la voie de circulation. Maintien d'un voie dans chaque direction.</description>
    <schedule>
      <start_date>2013-05-30</start_date>
      <end_date>2013-05-30</end_date>
    </schedule>
    <headline>Gaz m&#233;tropolitain</headline>
    <severity>2</severity>
    <roads>
      <road>
        <road_name>Lacombe</road_name>
        <from>Turenne</from>
        <to>Chatel</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.455426693000007,45.7653001316</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="36">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#232;te de la rue Ritchot</description>
    <schedule>
      <start_date>2013-05-29</start_date>
      <end_date>2013-05-29</end_date>
    </schedule>
    <headline>Excavation &#233;gout</headline>
    <severity>1</severity>
    <detour>Joliette, R&#233;gent et Renaud</detour>
    <roads>
      <road>
        <road_name>Ritchot</road_name>
        <from>Joliette</from>
        <to>Montcalm</to>
      </road>
    </roads>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.442283868800004,45.7487346359</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="35">
    <status>ARCHIVED</status>
    <description>Fermeture compl&#232;te de la voie de circulation.</description>
    <schedule>
      <start_date>2013-05-28</start_date>
      <end_date>2013-05-28</end_date>
    </schedule>
    <headline>Excavation &#233;gouts</headline>
    <severity>1</severity>
    <detour>Notre-Dame, Iberville et Philippe-Goulet</detour>
    <roads>
      <road>
        <road_name>Laurentien</road_name>
        <from>Rachel</from>
        <to>Rainville</to>
      </road>
    </roads>
    <event_type>INCIDENT</event_type>
    <geography>
      <gml:Point srsName="EPSG:4326">
        <gml:coordinates>-73.416336178799995,45.775317137599998</gml:coordinates>
      </gml:Point>
    </geography>
  </event>
  <event xml:lang="fr" id="37">
    <status>ACTIVE</status>
    <description>Fermeture compl&#232;te du chemin de la Presqu'Ile</description>
    <schedule>
      <start_date>2013-05-03</start_date>
      <end_date>2013-05-18</end_date>
    </schedule>
    <headline>R&#233;fection de pavage</headline>
    <severity>3</severity>
    <detour>Saint-Paul, Chemin de la Savane et mont&#233;e Lebeau</detour>
    <roads>
      <road>
        <road_name>Chemin de la Presqu'Ile</road_name>
        <from>Saint-Paul</from>
        <to>Mont&#233;e Lebeau</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.496990203899998,45.764589106499997 -73.493900299100005,45.768241433900002 -73.492012023900003,45.771384638900003 -73.491282463100006,45.772671805100003 -73.488922119099996,45.7782691357</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="38">
    <status>ACTIVE</status>
    <description>Fermeture compl&#232;te de voie de circulation en direction Nord</description>
    <schedule>
      <start_date>2013-06-03</start_date>
      <end_date>2013-06-29</end_date>
    </schedule>
    <headline>Travaux majeurs d'Aqueduc</headline>
    <severity>3</severity>
    <roads>
      <road>
        <road_name>Valmont</road_name>
        <from>Sarte</from>
        <to>Beauchesne/Masson</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.434194326400004,45.764431931300003 -73.435481786699995,45.764978300300001 -73.436640500999999,45.765502210800001</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="40">
    <status>ACTIVE</status>
    <description>Fermeture compl&#232;te de la voie de circulation.</description>
    <schedule>
      <start_date>2013-06-04</start_date>
      <end_date>2013-06-05</end_date>
    </schedule>
    <headline>Travaux de resurfacage</headline>
    <severity>2</severity>
    <detour>Lafortune</detour>
    <roads>
      <road>
        <road_name>Boulevard Lacombe</road_name>
        <from>Boulevard Le Bourg-Neuf</from>
        <to>Rue Lafortune</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.452250957499999,45.769393962999999 -73.453345298800002,45.7677175492 -73.454589843799994,45.7663554258</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="42">
    <status>ACTIVE</status>
    <description>Fermeture compl&#232;te de la voie de circulation</description>
    <schedule>
      <start_date>2013-06-07</start_date>
      <end_date>2013-06-10</end_date>
    </schedule>
    <headline>Train de l'Est</headline>
    <severity>3</severity>
    <detour>Rue Saint-Paul - Chemin de la Presqu'&#206;le et r&#233;seau local dans Charlemagne jusqu'&#224; rue de Lyon</detour>
    <roads>
      <road>
        <road_name>Boulevard Pierre - Le Gardeur</road_name>
        <from>Mont&#233;e des Arsenaux</from>
        <to>De Lyon</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.479566574100005,45.747941045399998 -73.485746383700004,45.737578413900003 -73.488407135000003,45.736619923100001 -73.490810394299999,45.735481693899999 -73.489265441900002,45.734583075499998</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="39">
    <status>ARCHIVED</status>
    <description>Fermeture partielle de la voie de circulation. Circulation en alternance avec signaleur. </description>
    <schedule>
      <start_date>2013-05-30</start_date>
      <end_date>2013-05-31</end_date>
    </schedule>
    <headline>Travaux de raccordement aux services d'&#233;gouts</headline>
    <severity>2</severity>
    <roads>
      <road>
        <road_name>Marquis</road_name>
        <from>Plaisance</from>
        <to>Brien</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.460780382199999,45.747956018899998 -73.461070060699996,45.747626600799997 -73.461359739299994,45.747252259699998</gml:coordinates>
      </gml:LineString>
    </geography>
  </event>
  <event xml:lang="fr" id="41">
    <status>ACTIVE</status>
    <description>Fermeture partiel de la voie de circulation.</description>
    <schedule>
      <start_date>2013-06-05</start_date>
      <end_date>2013-06-21</end_date>
    </schedule>
    <headline>Travaux de pavage pour la construction du piste cyclable.</headline>
    <severity>2</severity>
    <detour>Circulation en alternance avec la pr&#233;sence de signaleurs.</detour>
    <roads>
      <road>
        <road_name>Chemin de la Presqu'&#206;le</road_name>
        <from>Rue Nathalie</from>
        <to>Limite de la Ville de Repentigny et Charlemagne</to>
      </road>
    </roads>
    <event_type>CONSTRUCTION</event_type>
    <geography>
      <gml:LineString srsName="EPSG:4326">
        <gml:coordinates>-73.508405685400007,45.750875776500003 -73.510208129899993,45.7454254389 -73.511152267499995,45.742490421200003 -73.509521484399997,45.740333983399999 -73.501796722400002,45.736679829300002</gml:coordinates>
      </gml:LineString>
    </geography>
    <created>2013-06-05T13:50:54.229529+00:00</created>
    <updated>2013-06-05T15:12:38.896822+00:00</updated>
  </event>
</open511>
"""        

