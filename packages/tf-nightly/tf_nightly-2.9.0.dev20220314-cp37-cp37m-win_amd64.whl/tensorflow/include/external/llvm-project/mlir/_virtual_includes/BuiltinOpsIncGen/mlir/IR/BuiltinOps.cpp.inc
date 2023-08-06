/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Op Definitions                                                             *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

#ifdef GET_OP_LIST
#undef GET_OP_LIST

::mlir::FuncOp,
::mlir::ModuleOp,
::mlir::UnrealizedConversionCastOp
#endif  // GET_OP_LIST

#ifdef GET_OP_CLASSES
#undef GET_OP_CLASSES


//===----------------------------------------------------------------------===//
// Local Utility Method Definitions
//===----------------------------------------------------------------------===//

namespace mlir {

static ::mlir::LogicalResult __mlir_ods_local_type_constraint_BuiltinOps0(
    ::mlir::Operation *op, ::mlir::Type type, ::llvm::StringRef valueKind,
    unsigned valueIndex) {
  if (!((true))) {
    return op->emitOpError(valueKind) << " #" << valueIndex
        << " must be any type, but got " << type;
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_BuiltinOps0(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  if (attr && !((attr.isa<::mlir::StringAttr>()))) {
    return op->emitOpError("attribute '") << attrName
        << "' failed to satisfy constraint: string attribute";
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_attr_constraint_BuiltinOps1(
    ::mlir::Operation *op, ::mlir::Attribute attr, ::llvm::StringRef attrName) {
  if (attr && !(((attr.isa<::mlir::TypeAttr>())) && ((attr.cast<::mlir::TypeAttr>().getValue().isa<::mlir::FunctionType>())))) {
    return op->emitOpError("attribute '") << attrName
        << "' failed to satisfy constraint: type attribute of ";
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_region_constraint_BuiltinOps0(
    ::mlir::Operation *op, ::mlir::Region &region, ::llvm::StringRef regionName,
    unsigned regionIndex) {
  if (!((true))) {
    return op->emitOpError("region #") << regionIndex
        << (regionName.empty() ? " " : " ('" + regionName + "') ")
        << "failed to verify constraint: any region";
  }
  return ::mlir::success();
}

static ::mlir::LogicalResult __mlir_ods_local_region_constraint_BuiltinOps1(
    ::mlir::Operation *op, ::mlir::Region &region, ::llvm::StringRef regionName,
    unsigned regionIndex) {
  if (!((::llvm::hasNItems(region, 1)))) {
    return op->emitOpError("region #") << regionIndex
        << (regionName.empty() ? " " : " ('" + regionName + "') ")
        << "failed to verify constraint: region with 1 blocks";
  }
  return ::mlir::success();
}
} // namespace mlir
namespace mlir {

//===----------------------------------------------------------------------===//
// ::mlir::FuncOp definitions
//===----------------------------------------------------------------------===//

FuncOpAdaptor::FuncOpAdaptor(::mlir::ValueRange values, ::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsOperands(values), odsAttrs(attrs), odsRegions(regions) {}

FuncOpAdaptor::FuncOpAdaptor(FuncOp &op) : odsOperands(op->getOperands()), odsAttrs(op->getAttrDictionary()), odsRegions(op->getRegions()) {}

::mlir::ValueRange FuncOpAdaptor::getOperands() {
  return odsOperands;
}

std::pair<unsigned, unsigned> FuncOpAdaptor::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::ValueRange FuncOpAdaptor::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(odsOperands.begin(), valueRange.first),
           std::next(odsOperands.begin(), valueRange.first + valueRange.second)};
}

::mlir::DictionaryAttr FuncOpAdaptor::getAttributes() {
  return odsAttrs;
}

::mlir::StringAttr FuncOpAdaptor::getSymNameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_name").cast<::mlir::StringAttr>();
  return attr;
}

::llvm::StringRef FuncOpAdaptor::getSymName() {
  auto attr = getSymNameAttr();
  return attr.getValue();
}

::mlir::StringAttr FuncOpAdaptor::sym_nameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_name").cast<::mlir::StringAttr>();
  return attr;
}

::llvm::StringRef FuncOpAdaptor::sym_name() {
  auto attr = sym_nameAttr();
  return attr.getValue();
}

::mlir::TypeAttr FuncOpAdaptor::getTypeAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::TypeAttr attr = odsAttrs.get("type").cast<::mlir::TypeAttr>();
  return attr;
}

::mlir::FunctionType FuncOpAdaptor::getType() {
  auto attr = getTypeAttr();
  return attr.getValue().cast<::mlir::FunctionType>();
}

::mlir::TypeAttr FuncOpAdaptor::typeAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::TypeAttr attr = odsAttrs.get("type").cast<::mlir::TypeAttr>();
  return attr;
}

::mlir::FunctionType FuncOpAdaptor::type() {
  auto attr = typeAttr();
  return attr.getValue().cast<::mlir::FunctionType>();
}

::mlir::StringAttr FuncOpAdaptor::getSymVisibilityAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_visibility").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > FuncOpAdaptor::getSymVisibility() {
  auto attr = getSymVisibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr FuncOpAdaptor::sym_visibilityAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_visibility").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > FuncOpAdaptor::sym_visibility() {
  auto attr = sym_visibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::RegionRange FuncOpAdaptor::getRegions() {
  return odsRegions;
}

::mlir::Region &FuncOpAdaptor::getBody() {
  return *odsRegions[0];
}

::mlir::Region &FuncOpAdaptor::body() {
  return *odsRegions[0];
}

::mlir::LogicalResult FuncOpAdaptor::verify(::mlir::Location loc) {
  {
    auto tblgen_sym_name = odsAttrs.get("sym_name");
    if (!tblgen_sym_name)
      return emitError(loc, "'builtin.func' op ""requires attribute 'sym_name'");

    if (tblgen_sym_name && !((tblgen_sym_name.isa<::mlir::StringAttr>())))
      return emitError(loc, "'builtin.func' op ""attribute 'sym_name' failed to satisfy constraint: string attribute");
  }
  {
    auto tblgen_type = odsAttrs.get("type");
    if (!tblgen_type)
      return emitError(loc, "'builtin.func' op ""requires attribute 'type'");

    if (tblgen_type && !(((tblgen_type.isa<::mlir::TypeAttr>())) && ((tblgen_type.cast<::mlir::TypeAttr>().getValue().isa<::mlir::FunctionType>()))))
      return emitError(loc, "'builtin.func' op ""attribute 'type' failed to satisfy constraint: type attribute of ");
  }
  {
    auto tblgen_sym_visibility = odsAttrs.get("sym_visibility");
    if (tblgen_sym_visibility && !((tblgen_sym_visibility.isa<::mlir::StringAttr>())))
      return emitError(loc, "'builtin.func' op ""attribute 'sym_visibility' failed to satisfy constraint: string attribute");
  }
  return ::mlir::success();
}

std::pair<unsigned, unsigned> FuncOp::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range FuncOp::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> FuncOp::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range FuncOp::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &FuncOp::getBody() {
  return (*this)->getRegion(0);
}

::mlir::Region &FuncOp::body() {
  return (*this)->getRegion(0);
}

::mlir::StringAttr FuncOp::getSymNameAttr() {
  return (*this)->getAttr(getSymNameAttrName()).cast<::mlir::StringAttr>();
}

::llvm::StringRef FuncOp::getSymName() {
  auto attr = getSymNameAttr();
  return attr.getValue();
}

::mlir::StringAttr FuncOp::sym_nameAttr() {
  return (*this)->getAttr(sym_nameAttrName()).cast<::mlir::StringAttr>();
}

::llvm::StringRef FuncOp::sym_name() {
  auto attr = sym_nameAttr();
  return attr.getValue();
}

::mlir::TypeAttr FuncOp::getTypeAttr() {
  return (*this)->getAttr(getTypeAttrName()).cast<::mlir::TypeAttr>();
}

::mlir::FunctionType FuncOp::getType() {
  auto attr = getTypeAttr();
  return attr.getValue().cast<::mlir::FunctionType>();
}

::mlir::TypeAttr FuncOp::typeAttr() {
  return (*this)->getAttr(typeAttrName()).cast<::mlir::TypeAttr>();
}

::mlir::FunctionType FuncOp::type() {
  auto attr = typeAttr();
  return attr.getValue().cast<::mlir::FunctionType>();
}

::mlir::StringAttr FuncOp::getSymVisibilityAttr() {
  return (*this)->getAttr(getSymVisibilityAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > FuncOp::getSymVisibility() {
  auto attr = getSymVisibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr FuncOp::sym_visibilityAttr() {
  return (*this)->getAttr(sym_visibilityAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > FuncOp::sym_visibility() {
  auto attr = sym_visibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

void FuncOp::setSymNameAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(getSymNameAttrName(), attr);
}

void FuncOp::sym_nameAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(sym_nameAttrName(), attr);
}

void FuncOp::setTypeAttr(::mlir::TypeAttr attr) {
  (*this)->setAttr(getTypeAttrName(), attr);
}

void FuncOp::typeAttr(::mlir::TypeAttr attr) {
  (*this)->setAttr(typeAttrName(), attr);
}

void FuncOp::setSymVisibilityAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(getSymVisibilityAttrName(), attr);
}

void FuncOp::sym_visibilityAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(sym_visibilityAttrName(), attr);
}

::mlir::Attribute FuncOp::removeSym_visibilityAttr() {
  return (*this)->removeAttr(getSymVisibilityAttrName());
}

void FuncOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::StringAttr sym_name, ::mlir::TypeAttr type, /*optional*/::mlir::StringAttr sym_visibility) {
  odsState.addAttribute(getSymNameAttrName(odsState.name), sym_name);
  odsState.addAttribute(getTypeAttrName(odsState.name), type);
  if (sym_visibility) {
  odsState.addAttribute(getSymVisibilityAttrName(odsState.name), sym_visibility);
  }
  (void)odsState.addRegion();
}

void FuncOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::StringAttr sym_name, ::mlir::TypeAttr type, /*optional*/::mlir::StringAttr sym_visibility) {
  odsState.addAttribute(getSymNameAttrName(odsState.name), sym_name);
  odsState.addAttribute(getTypeAttrName(odsState.name), type);
  if (sym_visibility) {
  odsState.addAttribute(getSymVisibilityAttrName(odsState.name), sym_visibility);
  }
  (void)odsState.addRegion();
  assert(resultTypes.size() == 0u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void FuncOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::llvm::StringRef sym_name, ::mlir::FunctionType type, /*optional*/::mlir::StringAttr sym_visibility) {
  odsState.addAttribute(getSymNameAttrName(odsState.name), odsBuilder.getStringAttr(sym_name));
  odsState.addAttribute(getTypeAttrName(odsState.name), ::mlir::TypeAttr::get(type));
  if (sym_visibility) {
  odsState.addAttribute(getSymVisibilityAttrName(odsState.name), sym_visibility);
  }
  (void)odsState.addRegion();
}

void FuncOp::build(::mlir::OpBuilder &odsBuilder, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::llvm::StringRef sym_name, ::mlir::FunctionType type, /*optional*/::mlir::StringAttr sym_visibility) {
  odsState.addAttribute(getSymNameAttrName(odsState.name), odsBuilder.getStringAttr(sym_name));
  odsState.addAttribute(getTypeAttrName(odsState.name), ::mlir::TypeAttr::get(type));
  if (sym_visibility) {
  odsState.addAttribute(getSymVisibilityAttrName(odsState.name), sym_visibility);
  }
  (void)odsState.addRegion();
  assert(resultTypes.size() == 0u && "mismatched number of results");
  odsState.addTypes(resultTypes);
}

void FuncOp::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  assert(operands.size() == 0u && "mismatched number of parameters");
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  for (unsigned i = 0; i != 1; ++i)
    (void)odsState.addRegion();
  assert(resultTypes.size() == 0u && "mismatched number of return types");
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult FuncOp::verifyInvariantsImpl() {
  {
    auto tblgen_sym_name = (*this)->getAttr(getSymNameAttrName());
    if (!tblgen_sym_name)
      return emitOpError("requires attribute 'sym_name'");

    if (::mlir::failed(__mlir_ods_local_attr_constraint_BuiltinOps0(*this, tblgen_sym_name, "sym_name")))
      return ::mlir::failure();
  }
  {
    auto tblgen_type = (*this)->getAttr(getTypeAttrName());
    if (!tblgen_type)
      return emitOpError("requires attribute 'type'");

    if (::mlir::failed(__mlir_ods_local_attr_constraint_BuiltinOps1(*this, tblgen_type, "type")))
      return ::mlir::failure();
  }
  {
    auto tblgen_sym_visibility = (*this)->getAttr(getSymVisibilityAttrName());
    if (::mlir::failed(__mlir_ods_local_attr_constraint_BuiltinOps0(*this, tblgen_sym_visibility, "sym_visibility")))
      return ::mlir::failure();
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::makeMutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_BuiltinOps0(*this, region, "body", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult FuncOp::verifyInvariants() {
  if(::mlir::succeeded(verifyInvariantsImpl()) && ::mlir::succeeded(verify()))
    return ::mlir::success();
  return ::mlir::failure();
}

} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::FuncOp)

namespace mlir {

//===----------------------------------------------------------------------===//
// ::mlir::ModuleOp definitions
//===----------------------------------------------------------------------===//

ModuleOpAdaptor::ModuleOpAdaptor(::mlir::ValueRange values, ::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsOperands(values), odsAttrs(attrs), odsRegions(regions) {}

ModuleOpAdaptor::ModuleOpAdaptor(ModuleOp &op) : odsOperands(op->getOperands()), odsAttrs(op->getAttrDictionary()), odsRegions(op->getRegions()) {}

::mlir::ValueRange ModuleOpAdaptor::getOperands() {
  return odsOperands;
}

std::pair<unsigned, unsigned> ModuleOpAdaptor::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::ValueRange ModuleOpAdaptor::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(odsOperands.begin(), valueRange.first),
           std::next(odsOperands.begin(), valueRange.first + valueRange.second)};
}

::mlir::DictionaryAttr ModuleOpAdaptor::getAttributes() {
  return odsAttrs;
}

::mlir::StringAttr ModuleOpAdaptor::getSymNameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_name").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > ModuleOpAdaptor::getSymName() {
  auto attr = getSymNameAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOpAdaptor::sym_nameAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_name").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > ModuleOpAdaptor::sym_name() {
  auto attr = sym_nameAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOpAdaptor::getSymVisibilityAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_visibility").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > ModuleOpAdaptor::getSymVisibility() {
  auto attr = getSymVisibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOpAdaptor::sym_visibilityAttr() {
  assert(odsAttrs && "no attributes when constructing adapter");
  ::mlir::StringAttr attr = odsAttrs.get("sym_visibility").dyn_cast_or_null<::mlir::StringAttr>();
  return attr;
}

::llvm::Optional< ::llvm::StringRef > ModuleOpAdaptor::sym_visibility() {
  auto attr = sym_visibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::RegionRange ModuleOpAdaptor::getRegions() {
  return odsRegions;
}

::mlir::Region &ModuleOpAdaptor::getBodyRegion() {
  return *odsRegions[0];
}

::mlir::Region &ModuleOpAdaptor::bodyRegion() {
  return *odsRegions[0];
}

::mlir::LogicalResult ModuleOpAdaptor::verify(::mlir::Location loc) {
  {
    auto tblgen_sym_name = odsAttrs.get("sym_name");
    if (tblgen_sym_name && !((tblgen_sym_name.isa<::mlir::StringAttr>())))
      return emitError(loc, "'builtin.module' op ""attribute 'sym_name' failed to satisfy constraint: string attribute");
  }
  {
    auto tblgen_sym_visibility = odsAttrs.get("sym_visibility");
    if (tblgen_sym_visibility && !((tblgen_sym_visibility.isa<::mlir::StringAttr>())))
      return emitError(loc, "'builtin.module' op ""attribute 'sym_visibility' failed to satisfy constraint: string attribute");
  }
  return ::mlir::success();
}

std::pair<unsigned, unsigned> ModuleOp::getODSOperandIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::operand_range ModuleOp::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

std::pair<unsigned, unsigned> ModuleOp::getODSResultIndexAndLength(unsigned index) {
  return {index, 1};
}

::mlir::Operation::result_range ModuleOp::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Region &ModuleOp::getBodyRegion() {
  return (*this)->getRegion(0);
}

::mlir::Region &ModuleOp::bodyRegion() {
  return (*this)->getRegion(0);
}

::mlir::StringAttr ModuleOp::getSymNameAttr() {
  return (*this)->getAttr(getSymNameAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > ModuleOp::getSymName() {
  auto attr = getSymNameAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOp::sym_nameAttr() {
  return (*this)->getAttr(sym_nameAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > ModuleOp::sym_name() {
  auto attr = sym_nameAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOp::getSymVisibilityAttr() {
  return (*this)->getAttr(getSymVisibilityAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > ModuleOp::getSymVisibility() {
  auto attr = getSymVisibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

::mlir::StringAttr ModuleOp::sym_visibilityAttr() {
  return (*this)->getAttr(sym_visibilityAttrName()).dyn_cast_or_null<::mlir::StringAttr>();
}

::llvm::Optional< ::llvm::StringRef > ModuleOp::sym_visibility() {
  auto attr = sym_visibilityAttr();
  return attr ? ::llvm::Optional< ::llvm::StringRef >(attr.getValue()) : (::llvm::None);
}

void ModuleOp::setSymNameAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(getSymNameAttrName(), attr);
}

void ModuleOp::sym_nameAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(sym_nameAttrName(), attr);
}

void ModuleOp::setSymVisibilityAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(getSymVisibilityAttrName(), attr);
}

void ModuleOp::sym_visibilityAttr(::mlir::StringAttr attr) {
  (*this)->setAttr(sym_visibilityAttrName(), attr);
}

::mlir::Attribute ModuleOp::removeSym_nameAttr() {
  return (*this)->removeAttr(getSymNameAttrName());
}

::mlir::Attribute ModuleOp::removeSym_visibilityAttr() {
  return (*this)->removeAttr(getSymVisibilityAttrName());
}

::mlir::LogicalResult ModuleOp::verifyInvariantsImpl() {
  {
    auto tblgen_sym_name = (*this)->getAttr(getSymNameAttrName());
    if (::mlir::failed(__mlir_ods_local_attr_constraint_BuiltinOps0(*this, tblgen_sym_name, "sym_name")))
      return ::mlir::failure();
  }
  {
    auto tblgen_sym_visibility = (*this)->getAttr(getSymVisibilityAttrName());
    if (::mlir::failed(__mlir_ods_local_attr_constraint_BuiltinOps0(*this, tblgen_sym_visibility, "sym_visibility")))
      return ::mlir::failure();
  }
  {
    unsigned index = 0; (void)index;

    for (auto &region : ::llvm::makeMutableArrayRef((*this)->getRegion(0)))
      if (::mlir::failed(__mlir_ods_local_region_constraint_BuiltinOps1(*this, region, "bodyRegion", index++)))
        return ::mlir::failure();
  }
  return ::mlir::success();
}

::mlir::LogicalResult ModuleOp::verifyInvariants() {
  if(::mlir::succeeded(verifyInvariantsImpl()) && ::mlir::succeeded(verify()))
    return ::mlir::success();
  return ::mlir::failure();
}

::mlir::ParseResult ModuleOp::parse(::mlir::OpAsmParser &parser, ::mlir::OperationState &result) {
  ::mlir::StringAttr sym_nameAttr;
  std::unique_ptr<::mlir::Region> bodyRegionRegion = std::make_unique<::mlir::Region>();

  // Parsing an optional symbol name doesn't fail, so no need to check the
  // result.
  (void)parser.parseOptionalSymbolName(sym_nameAttr, "sym_name", result.attributes);
  if (sym_nameAttr) {
  }
  if (parser.parseOptionalAttrDictWithKeyword(result.attributes))
    return ::mlir::failure();

  if (parser.parseRegion(*bodyRegionRegion))
    return ::mlir::failure();

  if (bodyRegionRegion->empty()) bodyRegionRegion->emplaceBlock();
  result.addRegion(std::move(bodyRegionRegion));
  return ::mlir::success();
}

void ModuleOp::print(::mlir::OpAsmPrinter &_odsPrinter) {
  if ((*this)->getAttr("sym_name")) {
  _odsPrinter << ' ';
  _odsPrinter.printSymbolName(getSymNameAttr().getValue());
  }
  _odsPrinter.printOptionalAttrDictWithKeyword((*this)->getAttrs(), /*elidedAttrs=*/{"sym_name"});
  _odsPrinter << ' ';
  _odsPrinter.printRegion(getBodyRegion());
}

} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::ModuleOp)

namespace mlir {

//===----------------------------------------------------------------------===//
// ::mlir::UnrealizedConversionCastOp definitions
//===----------------------------------------------------------------------===//

UnrealizedConversionCastOpAdaptor::UnrealizedConversionCastOpAdaptor(::mlir::ValueRange values, ::mlir::DictionaryAttr attrs, ::mlir::RegionRange regions) : odsOperands(values), odsAttrs(attrs), odsRegions(regions) {}

UnrealizedConversionCastOpAdaptor::UnrealizedConversionCastOpAdaptor(UnrealizedConversionCastOp &op) : odsOperands(op->getOperands()), odsAttrs(op->getAttrDictionary()), odsRegions(op->getRegions()) {}

::mlir::ValueRange UnrealizedConversionCastOpAdaptor::getOperands() {
  return odsOperands;
}

std::pair<unsigned, unsigned> UnrealizedConversionCastOpAdaptor::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (odsOperands.size() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::ValueRange UnrealizedConversionCastOpAdaptor::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(odsOperands.begin(), valueRange.first),
           std::next(odsOperands.begin(), valueRange.first + valueRange.second)};
}

::mlir::ValueRange UnrealizedConversionCastOpAdaptor::getInputs() {
  return getODSOperands(0);
}

::mlir::ValueRange UnrealizedConversionCastOpAdaptor::inputs() {
  return getODSOperands(0);
}

::mlir::DictionaryAttr UnrealizedConversionCastOpAdaptor::getAttributes() {
  return odsAttrs;
}

::mlir::LogicalResult UnrealizedConversionCastOpAdaptor::verify(::mlir::Location loc) {
  return ::mlir::success();
}

std::pair<unsigned, unsigned> UnrealizedConversionCastOp::getODSOperandIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumOperands() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::operand_range UnrealizedConversionCastOp::getODSOperands(unsigned index) {
  auto valueRange = getODSOperandIndexAndLength(index);
  return {std::next(getOperation()->operand_begin(), valueRange.first),
           std::next(getOperation()->operand_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::operand_range UnrealizedConversionCastOp::getInputs() {
  return getODSOperands(0);
}

::mlir::Operation::operand_range UnrealizedConversionCastOp::inputs() {
  return getODSOperands(0);
}

::mlir::MutableOperandRange UnrealizedConversionCastOp::getInputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

::mlir::MutableOperandRange UnrealizedConversionCastOp::inputsMutable() {
  auto range = getODSOperandIndexAndLength(0);
  auto mutableRange = ::mlir::MutableOperandRange(getOperation(), range.first, range.second);
  return mutableRange;
}

std::pair<unsigned, unsigned> UnrealizedConversionCastOp::getODSResultIndexAndLength(unsigned index) {
  bool isVariadic[] = {true};
  int prevVariadicCount = 0;
  for (unsigned i = 0; i < index; ++i)
    if (isVariadic[i]) ++prevVariadicCount;

  // Calculate how many dynamic values a static variadic operand corresponds to.
  // This assumes all static variadic operands have the same dynamic value count.
  int variadicSize = (getOperation()->getNumResults() - 0) / 1;
  // `index` passed in as the parameter is the static index which counts each
  // operand (variadic or not) as size 1. So here for each previous static variadic
  // operand, we need to offset by (variadicSize - 1) to get where the dynamic
  // value pack for this static operand starts.
  int start = index + (variadicSize - 1) * prevVariadicCount;
  int size = isVariadic[index] ? variadicSize : 1;
  return {start, size};
}

::mlir::Operation::result_range UnrealizedConversionCastOp::getODSResults(unsigned index) {
  auto valueRange = getODSResultIndexAndLength(index);
  return {std::next(getOperation()->result_begin(), valueRange.first),
           std::next(getOperation()->result_begin(), valueRange.first + valueRange.second)};
}

::mlir::Operation::result_range UnrealizedConversionCastOp::getOutputs() {
  return getODSResults(0);
}

::mlir::Operation::result_range UnrealizedConversionCastOp::outputs() {
  return getODSResults(0);
}

void UnrealizedConversionCastOp::build(::mlir::OpBuilder &, ::mlir::OperationState &odsState, ::mlir::TypeRange resultTypes, ::mlir::ValueRange operands, ::llvm::ArrayRef<::mlir::NamedAttribute> attributes) {
  odsState.addOperands(operands);
  odsState.addAttributes(attributes);
  odsState.addTypes(resultTypes);
}

::mlir::LogicalResult UnrealizedConversionCastOp::verifyInvariantsImpl() {
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSOperands(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_BuiltinOps0(*this, v.getType(), "operand", index++)))
        return ::mlir::failure();
    }
  }
  {
    unsigned index = 0; (void)index;
    auto valueGroup0 = getODSResults(0);

    for (auto v : valueGroup0) {
      if (::mlir::failed(__mlir_ods_local_type_constraint_BuiltinOps0(*this, v.getType(), "result", index++)))
        return ::mlir::failure();
    }
  }
  return ::mlir::success();
}

::mlir::LogicalResult UnrealizedConversionCastOp::verifyInvariants() {
  return verifyInvariantsImpl();
}

::mlir::ParseResult UnrealizedConversionCastOp::parse(::mlir::OpAsmParser &parser, ::mlir::OperationState &result) {
  ::mlir::SmallVector<::mlir::OpAsmParser::OperandType, 4> inputsOperands;
  ::llvm::SMLoc inputsOperandsLoc;
  (void)inputsOperandsLoc;
  ::mlir::SmallVector<::mlir::Type, 1> inputsTypes;
  ::mlir::SmallVector<::mlir::Type, 1> outputsTypes;

  inputsOperandsLoc = parser.getCurrentLocation();
  if (parser.parseOperandList(inputsOperands))
    return ::mlir::failure();
  if (!inputsOperands.empty()) {
  if (parser.parseColon())
    return ::mlir::failure();

  if (parser.parseTypeList(inputsTypes))
    return ::mlir::failure();
  }
  if (parser.parseKeyword("to"))
    return ::mlir::failure();

  if (parser.parseTypeList(outputsTypes))
    return ::mlir::failure();
  if (parser.parseOptionalAttrDict(result.attributes))
    return ::mlir::failure();
  result.addTypes(outputsTypes);
  if (parser.resolveOperands(inputsOperands, inputsTypes, inputsOperandsLoc, result.operands))
    return ::mlir::failure();
  return ::mlir::success();
}

void UnrealizedConversionCastOp::print(::mlir::OpAsmPrinter &_odsPrinter) {
  if (!getInputs().empty()) {
  _odsPrinter << ' ';
  _odsPrinter << getInputs();
  _odsPrinter << ' ' << ":";
  _odsPrinter << ' ';
  _odsPrinter << getInputs().getTypes();
  }
  _odsPrinter << ' ' << "to";
  _odsPrinter << ' ';
  _odsPrinter << getOutputs().getTypes();
  _odsPrinter.printOptionalAttrDict((*this)->getAttrs(), /*elidedAttrs=*/{});
}

void UnrealizedConversionCastOp::getEffects(::mlir::SmallVectorImpl<::mlir::SideEffects::EffectInstance<::mlir::MemoryEffects::Effect>> &effects) {
}

} // namespace mlir
DEFINE_EXPLICIT_TYPE_ID(::mlir::UnrealizedConversionCastOp)


#endif  // GET_OP_CLASSES

