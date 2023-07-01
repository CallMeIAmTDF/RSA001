from Crypto.Util.number import *
#from flag import FLAG

p = getPrime(1024)
q = getPrime(1024)

#e = 65537
#n = p*q

#m = bytes_to_long(FLAG)

#c = pow(m, e, n)

#print(f'{p + q = }')
#print(f'{n = }')
#print(f'{c = }')
e = 65537
c = 5826352833734946581688492478038096734865879986530558407366391674142929329681319558528153354240786722608453710101055294752950592757054060564393943615708853429470836245046638403466916353579016978099047364033185522265970747739629580939169119628658752726878669690082006949932856920489696465815562403136437035809957619613645328908592111103271558005779916100275014911743691939679257812702559680612098721056928864480802907417919721909323173335536307292026226368030640159224623040941102274466498630393889171854641584781165775702884967230166325580236511331554706521236670501274110327211859624530134435395289597834913985359321
n = 14294289122144187333032197712732374108956653104712993512078258074371721278396695748572569973403476579636207923543858613953312531377785219875002414437782089325007574496321651874037425934006155019707092838054182223281372767343678984675070141519546463704886382257740876666207289744747431542027961334730445733414245072667028616384471709234617725457727050441795324625339895036969449958123214881364697025746666502130781819811974134261092372483219337747167938975782615028306142405438128362010964005296724524205597010895303727234430673586388507002349391884285642853223462021723257435033201604915019068056749471932066849543797
x = 243955297001875649110591178596664519421365583875937419955860634262572008253538872345495699896786789026251764371334547170212476149618376013444778474827527338147052428677920298268071440203885194814050988084198235457158014533528171242352737052474822770985257963673645191582394975053918021291330275164997228304682

phi = n - x + 1
d = inverse(e, phi)
m = pow(c, d, n)
m = hex(m)[2:]
print(bytes.fromhex(m))