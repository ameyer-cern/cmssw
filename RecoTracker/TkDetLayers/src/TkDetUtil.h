#ifndef TkDetLayers_TkDetUtil_h
#define TkDetLayers_TkDetUtil_h

#include "Geometry/CommonDetUnit/interface/GeomDet.h"
#include "TrackingTools/DetLayers/interface/MeasurementEstimator.h"
#include "DataFormats/GeometryVector/interface/GlobalPoint.h"
#include "TrackingTools/DetLayers/interface/rangesIntersect.h"
#include "DataFormats/GeometryVector/interface/VectorUtil.h"

class GeomDet;
class Plane;
class TrajectoryStateOnSurface;

#pragma GCC visibility push(hidden)

namespace tkDetUtil {

  inline bool overlapInPhi(float phi, const GeomDet& det, float phiWindow) {
    std::pair<float, float> phiRange(phi - phiWindow, phi + phiWindow);
    return rangesIntersect(phiRange, det.surface().phiSpan(), [](auto x, auto y) { return Geom::phiLess(x, y); });
  }

  inline bool overlapInPhi(GlobalPoint crossPoint, const GeomDet& det, float phiWindow) {
    return overlapInPhi(crossPoint.barePhi(), det, phiWindow);
  }

  float computeWindowSize(const GeomDet* det, const TrajectoryStateOnSurface& tsos, const MeasurementEstimator& est);

  float calculatePhiWindow(const MeasurementEstimator::Local2DVector& maxDistance,
                           const TrajectoryStateOnSurface& ts,
                           const Plane& plane);

}  // namespace tkDetUtil

#pragma GCC visibility pop
#endif  // TkDetLayers_TkDetUtil_h
